# AI 面试模拟官 — 使用指南

## 核心原则：先给简历和岗位，再开始面试

```
❌ 错误用法：不提供简历直接问"开始面试吧"
   → AI无法出题，因为没有你的背景信息

✅ 正确用法：先准备好简历.txt 和 岗位.txt
   → AI 读取后根据你的经历和岗位要求针对性提问
```

## 依赖

- Python 3.10+（仅标准库，无需 pip install）
- 免费大模型 API（默认 Ollama）

## 两步流程

```bash
# 第1步：准备好你的简历和岗位描述
#   简历.txt — 你的真实经历
#   岗位.txt — 你想面试的岗位要求

# 第2步：面试（-r 简历、-j 岗位 都是必填）
python scripts/interview.py -r 简历.txt -j 岗位.txt --mode normal

# 第3步：报告
python scripts/feedback.py --log interview_log.json -o report.md
```

## 面试示例

```bash
# 假设你有这两个文件：
#   my_resume.txt
#   target_job.txt

# 开始面试
python scripts/interview.py -r my_resume.txt -j target_job.txt --mode normal
```

## 免费 API 配置

### 方式 1：Ollama（完全免费，本地运行）

```bash
ollama pull qwen2.5
ollama serve
# config.json 已默认指向 http://localhost:11434/v1
```

### 方式 2：环境变量

```bash
$env:LLM_API_BASE="https://dashscope.aliyuncs.com/compatible-mode/v1"
$env:LLM_API_KEY="***"
```

面试中的命令：`/quit` 结束面试。

## 输出文件

| 文件 | 说明 |
|------|------|
| `interview_log.json` | 面试记录 |
| `interview_report.md` | 评分报告 |
