# AI 面试模拟官

> **选题**：AI个人系统实践 — AI面试模拟官
> **分类**：求职成长类

## AI 核心价值

传统面试准备无法针对个人简历动态生成定制问题并实时反馈。AI 面试官让每个人都拥有 24 小时在线的私人陪练——**而且不透露任何评价，确保你展现最真实的表现**。

## 功能简介

AI 扮演面试官，根据你的目标岗位和简历提出针对性问题、实时追问，**面试结束后**逐题评分、给出改进建议和参考思路。

| 功能 | 说明 |
|------|------|
| 个性化出题 | 基于简历+岗位生成问题，针对性强 |
| 实时追问 | 根据回答内容动态深入追问，面试官保持角色 |
| 面试后评分 | 面试结束后逐题评分 + 改进建议 + 参考思路 |
| 多面试模式 | normal / stress / mixed |

## 面试流程

### 第 1 步：准备你的简历和岗位

准备两个文本文件：

- `我的简历.txt` — 你的真实经历
- `目标岗位.txt` — 想面试的岗位描述

### 第 2 步：面试（只提问，不评分）

```bash
python skill/scripts/interview.py -r 我的简历.txt -j 目标岗位.txt --mode normal
```

AI 全程扮演面试官，只提问和追问，不透露任何评分或建议。

### 第 3 步：面试结束后评分

```bash
python skill/scripts/feedback.py --log interview_log.json -o report.md
```

逐题评分（1-10分）+ 改进建议 + 参考思路 + 综合总结。

## 项目结构

```
ai-interview-simulator/
├── skill/                        # Skill 文件
│   ├── SKILL.md                  # 技能定义文件
│   ├── scripts/                  # 脚本/工具代码
│   │   ├── interview.py          # 面试引擎（85行）
│   │   ├── resume_parser.py      # 简历解析（76行）
│   │   ├── feedback.py           # 评分报告（78行）
│   │   └── config.json           # 配置模板
│   └── references/               # 参考文件
│       ├── usage.md              # 使用指南
│       ├── prompts.md            # 提示词模板
│       ├── best-practices.md     # 最佳实践
│       └── interview-example.md  # 面试示例
├── data/                         # 测试数据
│   ├── sample_resume.txt         # 样本简历
│   ├── sample_job.txt            # 样本岗位
│   ├── test_cases.md             # 测试用例
│   ├── true_data/                # 测试截屏
│   ├── user_resume.txt           # 真实测试简历
│   ├── user_job.txt              # 真实测试岗位
│   ├── interview_log.json        # 真实面试记录
│   └── report.md                 # 真实评分报告
├── tests/                        # 测试记录
│   └── test_record.md            # 完整测试记录
├── iteration/                    # 迭代升级说明
│   └── iteration_log.md          # 5步迭代法 × 2
└── README.md                     # 本文件
```

## 面试模式

| 模式 | 说明 |
|------|------|
| normal | 标准面试，友好专业 |
| stress | 压力面试，持续追问质疑 |
| mixed | 先松后紧 |

## 依赖

- Python 3.10+（仅标准库，无需 pip）
- 免费大模型 API（默认 Ollama，支持千问/DeepSeek/OpenAI等）

## 迭代记录

详见 [`iteration/iteration_log.md`](iteration/iteration_log.md)

| 迭代 | 内容 |
|------|------|
| 迭代1 | 追问策略增强 — 5种追问类型，提升深挖深度 |
| 迭代2 | 多面试场景 + 减分项标记 |
| 规划中 | 个性化错题本 — 跨会话追踪薄弱点 |
