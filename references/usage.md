# AI 面试模拟官 — 使用指南

## 依赖

- Python 3.10+（仅标准库，无需 pip install）
- 免费大模型 API（默认 Ollama）

## 两步流程

```bash
# 第1步：面试
python scripts/interview.py -r resume.txt -j job.txt --mode normal

# 第2步：报告
python scripts/feedback.py --log interview_log.json -o report.md
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
