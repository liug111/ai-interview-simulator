# 测试用例

## 测试环境

- OS: Windows 11
- Python: 3.11
- LLM: 千问 DashScope（`qwen3.6-flash`）或 Ollama（`qwen2.5`）
- 依赖：仅标准库（无需 pip）

---

## 测试用例 1：标准模式面试

### 输入

| 参数 | 值 |
|------|-----|
| 简历 | `data/sample_resume.txt` |
| 岗位 | `data/sample_job.txt` |
| 模式 | `normal` |

### 命令

```bash
python scripts/interview.py -r data/sample_resume.txt -j data/sample_job.txt --mode normal
```

### 预期行为

1. AI 面试官根据简历中的电商项目经验提问
2. 用户回答后 AI 进行追问
3. 面试过程中不出现评分/评价/参考思路
4. 输入 `/quit` 可结束面试
5. 结束自动保存 `interview_log.json`

### 预期输出（interview_log.json）

```json
{
  "mode": "normal",
  "resume": "...",
  "job_desc": "...",
  "log": [
    {"round": 0, "type": "question", "role": "ai", "content": "..."},
    {"round": 1, "type": "answer", "role": "user", "content": "..."},
    {"round": 1, "type": "question", "role": "ai", "content": "..."}
  ]
}
```

---

## 测试用例 2：压力模式面试

### 输入

| 参数 | 值 |
|------|-----|
| 简历 | `data/sample_resume.txt` |
| 岗位 | `data/sample_job.txt` |
| 模式 | `stress` |

### 命令

```bash
python scripts/interview.py -r data/sample_resume.txt -j data/sample_job.txt --mode stress
```

### 预期行为

1. AI 面试官更严格，持续追问细节和质疑假设
2. 面试过程保持压力氛围

---

## 测试用例 3：混合模式面试

### 输入

| 参数 | 值 |
|------|-----|
| 简历 | `data/sample_resume.txt` |
| 岗位 | `data/sample_job.txt` |
| 模式 | `mixed` |

### 命令

```bash
python scripts/interview.py -r data/sample_resume.txt -j data/sample_job.txt --mode mixed
```

### 预期行为

1. 前 3 轮友好专业
2. 之后切换为压力风格

---

## 测试用例 4：面试后评分报告

### 前置条件

已通过测试用例 1-3 之一生成了 `interview_log.json`。

### 命令

```bash
python scripts/feedback.py --log interview_log.json -o report.md
```

### 预期输出

`report.md` 包含：
- 每轮独立评分（1-10 分）
- 改进建议
- 参考思路
- 综合总结（总分、趋势、优势、改进重点）

### 备用命令（无 LLM 时）

```bash
python scripts/feedback.py --log interview_log.json --no-llm
```

---

## 测试用例 5：简历解析

### 输入

```bash
python scripts/resume_parser.py data/sample_resume.txt
```

### 预期输出

解析后的 JSON，包含 contact、education、experience、projects、skills 等字段。
