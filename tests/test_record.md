# 测试记录

## 测试环境

| 项目 | 值 |
|------|-----|
| 操作系统 | Windows 11 |
| Python 版本 | 3.11.15 |
| 大模型 API | 千问 DashScope (`qwen3.6-flash`) |
| 工作目录 | `ai-interview-simulator/` |
| 测试日期 | 2026-07-11 |
| 被面试者 | LiuG（简历：嘉应学院·数据科学与大数据技术） |
| 目标岗位 | 大数据开发工程师（实习/应届） |

---

## 测试 1：标准模式面试（interview.py）

### 步骤

1. 提供用户简历 `tests/user_resume.txt`
2. 提供目标岗位 `tests/user_job.txt`
3. 运行 `python scripts/interview.py -r tests/user_resume.txt -j tests/user_job.txt --mode normal`
4. 用户回答 AI 的提问，AI 基于回答实时追问
5. 共完成 3 轮 Q&A

### 结果

✅ 面试过程完整，运行正常。观察到：

### 面试对话记录

**第 1 轮（AI 出题）**

AI 面试官基于简历中"泰迪公司"的实习经历和"数据分析+AI"关键词，针对性提问项目详情。

**用户回答要点**：STAR 法则结构完整，"销售工单响应优化"项目，数据来源、清洗三类问题（乱码/重复/缺失）、技术栈（Python/Pandas/LightGBM/Flask/Streamlit）、量化成果（成交周期-12%，转化率+21%）、工程化思维（飞书监控、人工复核）。

**AI 追问**：假设数据规模扩展到 TB 级，设计 HDFS/Spark/Hive 架构。

**第 2 轮**

**用户回答要点**：HDFS 存储底座、Hive 三层数仓（ODS/DWD/DWS/Parquet）、Spark 计算、Airflow 调度。

**AI 追问**：Spark 资源调优，OOM 与数据倾斜处理，SHAP 分布式策略。

**第 3 轮**

**用户回答要点**：Executor 配置（4-8核/8-16GB）、分区控制（200-500 partitions）、两阶段聚合加盐、SHAP 分批+KernelSHAP 近似、Spark UI 监控。

**AI 第 4 问准备中，用户选择结束** ✅ 追问链连续性良好。

### 追问链深度

```
项目介绍 → 架构设计 → 资源调优 → 故障排查（未答）
```
追问链长度：3 轮，自然衔接，AI 保持面试官角色，全程不透露评分。

---

## 测试 2：评分报告（feedback.py）

### 命令

```bash
python scripts/feedback.py --log interview_log.json -o report.md
```

### 结果

✅ 逐题评分 + 改进建议 + 参考思路 + 综合总结 全部生成。

### 评分结果

| 轮次 | 评分 | 不足 | 参考思路要点 |
|------|------|------|------------|
| 第1轮 项目描述 | **9/10** | 未明确采集手段（Flume/Kafka） | 采集→清洗→加工→应用→迭代主线 |
| 第2轮 架构设计 | **8/10** | 缺采集层，未提 Iceberg/Hudi | 补充端到端链路 + Lakehouse |
| 第3轮 资源调优 | **8.5/10** | 内存偏保守，分区应动态计算 | AQE + Checkpoint + 分区公式 |

**总分平均：8.5/10**

### 综合总结摘要

- **关键优势**：结构化表达、数仓分层认知、Spark 调优经验、全链路意识
- **改进重点**：现代数仓（Iceberg/Hudi）、采集层补位、参数科学化

---

## 测试 3：简历解析（resume_parser.py）

### 命令

```bash
python scripts/resume_parser.py tests/user_resume.txt
```

### 结果

✅ 成功解析出教育背景、实习经历、技能列表等结构化信息。

---

## 测试总结

| 测试用例 | 状态 | 备注 |
|----------|------|------|
| 标准模式面试（interview.py） | ✅ 通过 | 共 3 轮 Q&A，追问链连续，AI 保持角色 |
| 评分报告（feedback.py） | ✅ 通过 | 逐题评分+综合总结，总分 8.5/10 |
| 简历解析（resume_parser.py） | ✅ 通过 | 结构化字段完整 |
| **所有文件行数 < 150** | ✅ 通过 | 最大 85 行 |
| **零依赖** | ✅ 通过 | 仅 Python 标准库 |

**总体结论**：AI 面试模拟官功能正常。AI 能基于用户简历和岗位出题、基于回答动态追问、面试后逐题评分+建议+参考。符合设计要求。
