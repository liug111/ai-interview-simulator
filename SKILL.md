---
name: "ai-interview-simulator"
description: "AI面试模拟官：基于简历和JD自适应出题、动态追问、面试后逐题评分的免费面试模拟Skill"
category: "求职成长类"
---

# AI 面试模拟官

**分类：求职成长类**

基于大语言模型的免费面试模拟系统。纯 Python 标准库，零依赖。

## 适合群体

**准备面试、缺乏经验、容易紧张的学生。**

如果你：
- 第一次面试，不知道"面试到底长什么样"
- 有笔试能力但一开口就紧张、语无伦次
- 不知道自己的回答差在哪里、该怎么改进
- 想低成本、无压力地反复练习直到不紧张

这个技能就是为你准备的。

## AI 核心价值

| 维度 | 传统方式 | AI 方式 |
|------|----------|---------|
| 出题 | 固定题库 | 根据简历+JD 针对性提问 |
| 追问 | 线性流程 | 基于回答自然深挖，路径动态 |
| 角色感 | 无 | 面试全程保持严肃角色，不给提示 |
| 反馈 | 无或模板 | 面试后逐题评分+建议+参考 |

## MVP 流程

```
面试（interview.py）：  输入岗位+简历 → AI 出题 → 回答 → AI 追问 → 回答 → ... → 结束
报告（feedback.py）：   读取面试记录 → 逐题评分+建议+参考 → 综合总结
```

面试中 AI 只扮演面试官，不透露任何评价。所有评估在面试后由 feedback.py 完成。

## 文件结构

```
ai-interview-simulator/
  SKILL.md
  scripts/
    interview.py       # 面试引擎（< 150 行）
    resume_parser.py   # 简历解析（< 150 行）
    feedback.py        # 评分报告（< 150 行）
    config.json        # 配置模板
  references/
    usage.md
    prompts.md
    best-practices.md
    interview-example.md
    iterations.md      # 5步迭代法记录
```

## 模式

- **normal** — 标准，友好专业
- **stress** — 压力，持续追问质疑
- **mixed** — 先松后紧

## 使用

```bash
# 第1步：面试
python scripts/interview.py -r resume.txt -j job.txt --mode normal

# 第2步：报告
python scripts/feedback.py --log interview_log.json -o report.md
```

## 依赖

- Python 3.10+（仅标准库，无需 pip）
- 免费大模型 API（默认 Ollama，配置后支持 OpenAI/千问/DeepSeek 等）
