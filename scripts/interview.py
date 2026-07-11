#!/usr/bin/env python3
"""AI面试模拟官 - 面试引擎（零依赖，<150行）

⚠️ 必须先由用户提供自己的简历(-r)和目标岗位(-j)，AI再基于这些内容出题。
   没有简历和岗位信息，AI 无法开始面试。
"""
import json, os, sys, argparse, urllib.request

MODES = {
    "normal": {"name": "标准面试", "personality": "保持专业友好，深入挖掘。"},
    "stress": {"name": "压力面试", "personality": "持续质疑追问，制造紧张感。"},
    "mixed": {"name": "混合面试", "personality": "前3轮友好，之后切换为压力风格。"}
}
SYSTEM_TPL = \
"你是一名面试官，正在为以下岗位招聘。\n\n" \
"【模式】{mode}\n" \
"【岗位】\n{jd}\n\n" \
"【简历】\n{resume}\n\n" \
"行为：1)从最相关的点提问，每次一问 2)基于回答追问 3){personality}\n" \
"4)结束时输出 【面试结束】\n" \
"⚠️ 只提问，不评分、不评价、不给建议。"


def call_llm(messages, cfg):
    key = os.environ.get(cfg.get("key_env", "LLM_API_KEY"), cfg.get("key", ""))
    base = os.environ.get(cfg.get("base_env", "LLM_API_BASE"), cfg.get("base", ""))
    if not base:
        raise SystemExit("❌ 未设置 LLM_API_BASE 环境变量或 config.json 中的 base")
    data = json.dumps({"model": cfg.get("model", "qwen2.5"), "messages": messages,
        "temperature": cfg.get("temperature", 0.7), "max_tokens": cfg.get("max_tokens", 2048)}).encode()
    req = urllib.request.Request(f"{base.rstrip('/')}/chat/completions", data=data,
        headers={"Content-Type": "application/json"}, method="POST")
    if key:
        req.add_header("Authorization", f"Bearer {key}")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def load_cfg(path):
    with open(path, encoding="utf-8") as f:
        c = json.load(f)
    c["key"] = os.environ.get(c.get("key_env", "LLM_API_KEY"), c.get("key", ""))
    c["base"] = os.environ.get(c.get("base_env", "LLM_API_BASE"), c.get("base", "http://localhost:11434/v1"))
    return c


def main():
    ap = argparse.ArgumentParser(description="AI面试模拟官 - 面试引擎")
    ap.add_argument("--config", default="config.json")
    ap.add_argument("--resume", "-r", required=True, help="(必填) 你的简历文本或文件路径 — AI 据此出题")
    ap.add_argument("--jd", "-j", required=True, help="(必填) 目标岗位描述文本或文件路径 — AI 据此针对性提问")
    ap.add_argument("--mode", choices=list(MODES.keys()), default="normal")
    ap.add_argument("--log", default="interview_log.json")
    args = ap.parse_args()

    def rf(p):
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as f:
                return f.read()
        return p

    cfg = load_cfg(args.config)
    resume, jd = rf(args.resume), rf(args.jd)
    mi = MODES[args.mode]

    print(f"\n{'=' * 55}\n  AI 面试模拟官 — {mi['name']}\n{'=' * 55}")
    print("💡 输入 /quit 结束\n")

    sys_prompt = SYSTEM_TPL.format(mode=args.mode, jd=jd, resume=resume, personality=mi["personality"])
    hist = [{"role": "system", "content": sys_prompt}]
    log = []
    rnd = 0

    first = call_llm([hist[0]], cfg)
    hist.append({"role": "assistant", "content": first})
    log.append({"round": rnd, "type": "question", "role": "ai", "content": first})
    print(f"🎯 面试官: {first}\n")

    while True:
        try:
            ans = input("📝 你: ")
        except (EOFError, KeyboardInterrupt):
            break
        if ans.strip().lower() in ("/quit", "/exit", "/end"):
            break
        rnd += 1
        hist.append({"role": "user", "content": ans})
        log.append({"round": rnd, "type": "answer", "role": "user", "content": ans})
        resp = call_llm(hist, cfg)
        hist.append({"role": "assistant", "content": resp})
        log.append({"round": rnd, "type": "question", "role": "ai", "content": resp})
        print(f"\n🎯 面试官: {resp}\n")
        if "【面试结束】" in resp:
            print("✅ 面试已结束。")
            break

    with open(args.log, "w", encoding="utf-8") as f:
        json.dump({"mode": args.mode, "resume": resume, "job_desc": jd, "log": log}, f, ensure_ascii=False, indent=2)
    print(f"✅ 记录已保存至 {args.log}")
    print(f"💡 运行: python scripts/feedback.py --log {args.log} -o report.md")


if __name__ == "__main__":
    main()
