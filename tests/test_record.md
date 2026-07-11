# 测试记录

## 测试环境

| 项目 | 值 |
|------|-----|
| 操作系统 | Windows 11 |
| Python 版本 | 3.11.5 |
| 大模型 API | 千问 DashScope (`qwen3.6-flash`) |
| 工作目录 | `ai-interview-simulator/` |
| 测试日期 | 2026-07-11 |

---

## 测试 1：简历解析

### 步骤

1. 运行 `python scripts/resume_parser.py data/sample_resume.txt`

### 结果

✅ 成功。解析出结构化信息：
- 联系方式：邮箱、手机号 ✓
- 教育背景：某大学 计算机科学 本科 ✓
- 工作经历：电商平台 Python 后端 ✓
- 技能列表：Python, Django, Redis, MySQL, Git, Linux, Docker ✓

---

## 测试 2：标准模式面试（interview.py）

### 步骤

1. 配置环境变量指向免费 API
2. 运行 `python scripts/interview.py -r data/sample_resume.txt -j data/sample_job.txt --mode normal`
3. 回答 AI 的提问，模拟 3-5 轮对话
4. 输入 `/quit` 结束

### 结果

✅ 成功。观察到：
- AI 根据简历中的"电商项目"和"订单模块"进行针对性提问 ✓
- 追问内容基于上一轮回答动态生成 ✓
- 面试过程中没有出现评分/建议/参考 ✓
- 结束自动保存 interview_log.json ✓

### 日志文件

```
logs/interview_log.json  — 面试全程记录
```

---

## 测试 3：压力模式面试

### 步骤

```bash
python scripts/interview.py -r data/sample_resume.txt -j data/sample_job.txt --mode stress
```

### 结果

✅ 成功。AI 提问风格更严格：
- 持续追问细节要求证明 ✓
- 对模糊回答提出质疑 ✓

---

## 测试 4：评分报告（feedback.py）

### 步骤

```bash
python scripts/feedback.py --log interview_log.json -o report.md
```

### 结果

✅ 成功。报告内容：
- 逐题评分 ✓
- 改进建议 ✓
- 参考思路 ✓
- 综合总结（总分、趋势、优势、改进重点）✓

### 输出文件

```
report.md  — 完整评分报告
```

---

## 测试 5：快速统计（无 LLM 备用）

### 步骤

```bash
python scripts/feedback.py --log interview_log.json --no-llm
```

### 结果

✅ 成功。输出快速统计 JSON（默认评分 7 分，含提示）。

---

## 测试总结

| 测试用例 | 状态 | 备注 |
|----------|------|------|
| 简历解析 | ✅ 通过 | 结构化字段完整 |
| 标准模式面试 | ✅ 通过 | 追问自然，AI 保持角色 |
| 压力模式面试 | ✅ 通过 | 追问更严格 |
| 评分报告 | ✅ 通过 | 逐题评分+综合总结 |
| 快速统计备用 | ✅ 通过 | 无 LLM 可用时正常工作 |

**总体结论**：AI 面试模拟官 MVP 功能运行正常，符合设计要求。
