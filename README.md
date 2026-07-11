# AI 面试模拟官 — AI Interview Simulator

> **选题**：AI个人系统实践 — AI面试模拟官
>
> **AI 核心价值**：传统面试准备无法针对个人简历动态生成定制问题并实时反馈。AI 面试官让每个人都拥有 24 小时在线的私人陪练。

## 📋 功能简介

基于大语言模型的模拟面试工具，AI 扮演面试官，根据你的目标岗位和简历提出针对性问题、实时追问、评分反馈。

### 核心功能

| 功能 | 说明 |
|------|------|
| 🎯 个性化出题 | 基于简历+岗位生成问题，针对性强 |
| 🔄 实时追问 | 根据回答内容动态深入追问 |
| 📊 评分反馈 | 每题 1-10 分 + 扣分项 + 改进建议 + 参考思路 |
| 🎭 多面试类型 | 技术面 / HR面 / 压力面 / 群面 |
| 🔌 多 API 支持 | 阿里千问、DeepSeek 等免费大模型 |

## 🚀 快速使用

### 环境准备

```bash
# 1. 设置 API Key（以阿里千问为例）
set ALI_QWEN_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 2. 准备简历（txt/md 格式）
# 3. 运行
python skill/scripts/interview_simulator.py -p "Java后端开发" -r resume.txt -t "技术面"
```

### 交互式运行

```bash
python skill/scripts/interview_simulator.py
# 按提示输入目标岗位和简历即可
```

## 📁 项目结构

```
ai-interview-simulator/
├── skill/                        # Skill 文件
│   ├── SKILL.md                  # 技能定义（Hermes Agent 格式）
│   ├── scripts/
│   │   └── interview_simulator.py # 主脚本（98行，< 150行要求）
│   └── references/
│       ├── config_example.md     # API 配置参考
│       └── usage_guide.md        # 详细使用指南
├── data/                         # 测试数据
│   ├── sample_resume.md          # 示例简历
│   └── test_cases.md             # 测试用例
├── tests/                        # 测试记录
│   └── test_record.md            # 执行测试的详细记录
├── iteration/                    # 迭代升级说明
│   └── iteration_log.md          # 2 轮迭代（5步法）
└── README.md                     # 本文件
```

## 📊 面试流程

```
【提问】→ 你回答 → 【追问】→ 你回答 → 【评分】→ 下一题 → … → 【总结】
```

## 🛠 技术栈

- Python 3.8+ (标准库, 无第三方依赖)
- 阿里千问 DashScope / DeepSeek 大模型 API

## 📝 迭代记录

详见 [`iteration/iteration_log.md`](iteration/iteration_log.md)

### 已完成迭代

| 迭代 | 内容 |
|------|------|
| 迭代1 | 解决 AI 流程紊乱：结构化 prompt + 格式标记 + 轮次控制 |
| 迭代2 | 增加多面试类型：技术面/HR面/压力面/群面 |

### 规划中

- 历史回答分析 → 高频问题专项训练
- 真实面试问题回录 → 个人问题库
- Web 界面 / 报告导出

## 📦 提交信息

- **选题**：AI 面试模拟官
- **分类**：求职成长
- **技能框架**：Hermes Agent Skill (SKILL.md + scripts/ + references/)
