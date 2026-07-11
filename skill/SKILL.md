---
name: ai-interview-simulator
description: "AI 面试模拟官：输入目标岗位和简历，AI 扮演面试官进行模拟面试，支持技术面/HR面/压力面/群面，实时追问并给出评分与改进建议"
metadata:
  author: "AI个人系统实践"
  version: "1.0.0"
  license: "MIT"
allowed-tools:
  - exec
  - read
  - write
user-invocable: true
---

# AI 面试模拟官 (AI Interview Simulator)

## 概述

AI 面试模拟官是一个基于大语言模型的技能，用于模拟真实面试场景。它扮演面试官角色，根据你的目标岗位和简历内容，提出针对性的面试问题，实时追问，并在每题结束后给出评分和改进建议。

## AI 核心价值

**没有 AI 这个功能根本做不到。** 传统面试准备方式（看面经、背题库）无法针对个人简历和岗位动态生成定制问题、实时追问、并给出带具体改进建议的评分。AI 面试官让每个人都拥有一个 24 小时在线的、耐心的、客观的私人陪练。

## 功能特性

- **多面试类型**：技术面、HR面、压力面、群面
- **个性化出题**：基于你的简历和目标岗位生成问题
- **实时追问**：根据你的回答展开追问，模拟真实面试节奏
- **评分反馈**：每轮问答后给出 1-10 分评分 + 具体改进建议 + 参考思路
- **多 API 支持**：支持阿里千问 (DashScope)、DeepSeek 等免费大模型

## 使用方式

### 方式一：命令行直接运行

```bash
python scripts/interview_simulator.py --position "后端开发工程师" --resume "resume.txt" --type "技术面"
```

### 方式二：交互式输入

```bash
python scripts/interview_simulator.py
# 然后按提示输入目标岗位和简历内容
```

### 方式三：在 Agent 中调用

```python
# 通过 exec 工具调用脚本
exec(command="python skills/ai-interview-simulator/scripts/interview_simulator.py --position '产品经理' --resume 'resume.txt' --type 'HR面'")
```

## 环境要求

- Python 3.8+
- 免费大模型 API（阿里千问 / DeepSeek 等）

## 配置

设置 API Key 环境变量：

```bash
# 阿里千问（推荐，国内直连）
set ALI_QWEN_API_KEY=your_api_key_here

# 或 DeepSeek
set DEEPSEEK_API_KEY=your_api_key_here
```

详见 `references/config_example.md`

## 项目结构

```
ai-interview-simulator/
├── skill/
│   ├── SKILL.md                 # 本技能定义文件
│   ├── scripts/
│   │   └── interview_simulator.py  # 面试模拟主脚本
│   └── references/
│       ├── config_example.md       # 配置参考
│       └── usage_guide.md          # 使用指南
├── data/                          # 测试数据
├── tests/                         # 测试记录
├── iteration/                     # 迭代日志
└── README.md                      # 项目说明
```
