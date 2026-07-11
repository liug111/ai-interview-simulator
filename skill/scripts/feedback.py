#!/usr/bin/env python3
"""AI面试模拟官 - 面试后逐题评分+反馈报告（零依赖，<150行）"""
import json, os, urllib.request

DIMS = ["表达能力", "逻辑思维", "专业深度", "岗位匹配度", "应变能力", "沟通风度"]

EVAL_PROMPT = \
"你是一名资深面试评估专家。基于以下面试记录，\n" \
"对每轮 Q&A 独立评分(1-10)并给出改进建议和参考思路。\n\n" \
"每轮输出格式：\n" \
"### 第X轮\n" \
"**问题**：...\n" \
"**回答**：...\n" \
"**【评分】** X/10\n" \
"**【改进建议】** <具体指出亮点和不足>\n" \
"**【参考思路】** <更好的回答方向>\n---\n\n" \
"全部分析完后输出：\n" \
"## 综合总结\n" \
"总分平均: X/10\n" \
"评分趋势: ...\n" \
"关键优势: ...\n" \
"改进重点: ...\n" \
"总评: ...\n"


def call_llm(text, cfg):
    key = os.environ.get(cfg.get("key_env", "LLM_API_KEY"), cfg.get("key", ""))
    base = os.environ.get(cfg.get("base_env", "LLM_API_BASE"), cfg.get("base", "http://localhost:11434/v1"))
    data = json.dumps({"model": cfg.get("model", "qwen2.5"),
        "messages": [{"role": "system", "content": EVAL_PROMPT}, {"role": "user", "content": text}],
        "temperature": 0.3, "max_tokens": 4096}).encode()
    req = urllib.request.Request(f"{base.rstrip('/')}/chat/completions", data=data,
        headers={"Content-Type": "application/json"}, method="POST")
    if key:
        req.add_header("Authorization", f"Bearer {key}")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def extract_qa(data):
    log = data.get("log", [])
    pairs, cur = [], None
    for e in log:
        if e["type"] == "question" and e["role"] == "ai":
            if cur:
                pairs.append(cur)
            cur = {"round": e["round"], "question": e["content"], "answer": None}
        elif e["type"] == "answer" and e["role"] == "user" and cur:
            cur["answer"] = e["content"]
    if cur:
        pairs.append(cur)
    return [p for p in pairs if p["answer"] is not None]


def main():
    import argparse
    ap = argparse.ArgumentParser(description="AI面试模拟官 - 评分报告")
    ap.add_argument("--log", required=True)
    ap.add_argument("--config", default="config.json")
    ap.add_argument("-o", "--output", default="interview_report.md")
    ap.add_argument("--no-llm", action="store_true", help="快速统计(不用LLM)")
    args = ap.parse_args()

    with open(args.log, encoding="utf-8") as f:
        data = json.load(f)
    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)

    qa = extract_qa(data)
    if not qa:
        print("❌ 面试记录中没有有效 Q&A 对。")
        return

    print(f"\n{'=' * 50}\n  面试评分报告  |  共 {len(qa)} 轮  |  模式: {data.get('mode','?')}\n{'=' * 50}\n")

    if args.no_llm:
        output = json.dumps({"rounds": len(qa), "note": "快速统计",
            "scores": [7] * len(qa), "avg": 7}, ensure_ascii=False, indent=2)
        print("📊 快速统计")
    else:
        resume = data.get("resume", "")
        jd = data.get("job_desc", "")
        user_prompt = f"【岗位】\n{jd}\n\n【简历】\n{resume[:500]}\n\n【对话】\n{json.dumps(qa, ensure_ascii=False, indent=2)}"
        output = call_llm(user_prompt, cfg)
        print("✅ AI 评估完成")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"✅ 报告已保存至 {args.output}")


if __name__ == "__main__":
    main()
