#!/usr/bin/env python3
"""AI面试模拟官 - 基于大模型API的模拟面试工具"""
import json, os, sys, urllib.request, urllib.error

# ======== 配置区 ========
APIS = {
    "dashscope": {  # 阿里千问（推荐，国内直连）
        "url": "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        "key_env": "ALI_QWEN_API_KEY", "model": "qwen3.6-flash",
    },
    "deepseek": {
        "url": "https://api.deepseek.com/chat/completions",
        "key_env": "DEEPSEEK_API_KEY", "model": "deepseek-chat",
    },
}
TYPE_PROMPTS = {
    "技术面": "你是资深技术面试官，追问技术细节、考察深度。要求给出具体技术方案和代码理解。",
    "HR面": "你是HR面试官，考察综合素质、团队协作、职业规划。关注沟通表达和逻辑性。",
    "压力面": "你是压力面试官，不断质疑、打断、反问，测试抗压能力和应变能力。",
    "群面": "你是群面面试官，模拟无领导小组讨论，给出讨论题目并点评表现。",
}

def call_llm(messages, api="dashscope"):
    cfg = APIS.get(api)
    if not cfg: return f"不支持的API: {api}"
    key = os.environ.get(cfg["key_env"])
    if not key: return f"请设置环境变量 {cfg['key_env']}"
    body = json.dumps({"model": cfg["model"], "messages": messages,
        "temperature": 0.7, "stream": False}).encode()
    req = urllib.request.Request(cfg["url"], data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {key}")
    try:
        resp = urllib.request.urlopen(req, timeout=60)
        return json.loads(resp.read())["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        return f"API错误 {e.code}: {e.read().decode(errors='replace')}"
    except Exception as e:
        return f"调用失败: {e}"

def build_sysprompt(i_type, position, resume):
    style = TYPE_PROMPTS.get(i_type, TYPE_PROMPTS["技术面"])
    return (
        f"你是AI面试模拟官，模拟真实面试场景。\n"
        f"面试类型：{i_type}\n目标岗位：{position}\n候选人简历：{resume}\n\n"
        f"{style}\n\n"
        f"【执行流程】\n"
        f"1. 首轮直接提出第1个问题，标记【提问1】\n"
        f"2. 等待候选人回答后，如果回答有问题或可深入，先【追问】，标记【追问1】\n"
        f"3. 追问完毕后，输出【评分1】= 分数(1-10) + 扣分项 + 改进建议 + 参考思路\n"
        f"4. 然后提出下一题【提问2】，重复流程\n"
        f"5. 至少完成3个问题。最后输出【总结】= 整体评价+薄弱项+提升建议\n"
        f"严格遵守标记格式，每次回复只做一个动作。"
    )

def interview_loop(position, resume, i_type, api):
    print(f"\n{'='*50}\n  AI面试模拟官 - {i_type}\n  目标岗位: {position}\n{'='*50}\n")
    print("输入你的回答 → 回车提交 | exit=退出 | summary=跳过剩余直接总结\n")
    msgs = [{"role": "system", "content": build_sysprompt(i_type, position, resume)}]
    turn = 0
    while True:
        reply = call_llm(msgs, api)
        if reply.startswith("API错误") or reply.startswith("请设置") or reply.startswith("不支持的") or reply.startswith("调用失败"):
            print(f"\n[!] {reply}"); break
        print(f"\n[面试官] {reply}\n")
        msgs.append({"role": "assistant", "content": reply})
        turn += 1
        if turn >= 30:  # 安全上限
            print("\n[!] 已达最大轮数，结束面试。"); break
        while True:
            inp = input("🙋 你的回答: ").strip()
            if inp.lower() == "exit": return
            if inp.lower() == "summary":
                msgs.append({"role": "user", "content": "请给出整体总结评价和改进建议。"})
                s = call_llm(msgs, api)
                print(f"\n[面试官总结] {s}\n") if s else None
                return
            if inp: break
            print("回答不能为空，请重新输入或输入 exit 退出。")
        msgs.append({"role": "user", "content": inp})

def main():
    import argparse
    p = argparse.ArgumentParser(description="AI面试模拟官")
    p.add_argument("--position", "-p", help="目标岗位")
    p.add_argument("--resume", "-r", help="简历文本或简历文件路径")
    p.add_argument("--type", "-t", choices=list(TYPE_PROMPTS.keys()), default="技术面")
    p.add_argument("--api", choices=list(APIS.keys()), default="dashscope")
    args = p.parse_args()
    pos = args.position or input("目标岗位: ").strip()
    res = args.resume or input("简历内容或文件路径: ").strip()
    if os.path.isfile(res):
        with open(res, "r", encoding="utf-8") as f: res = f.read()
    elif args.resume and os.path.isfile(args.resume):
        with open(args.resume, "r", encoding="utf-8") as f: res = f.read()
    interview_loop(pos, res, args.type, args.api)

if __name__ == "__main__":
    main()
