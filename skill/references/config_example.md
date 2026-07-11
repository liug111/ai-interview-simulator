# 配置参考

## 支持的 API

| API | 配置环境变量 | 模型 | 获取方式 |
|-----|------------|------|---------|
| 阿里千问 DashScope | `ALI_QWEN_API_KEY` | qwen3.6-flash | [阿里云百炼](https://bailian.console.aliyun.com/) → 模型广场 → API-KEY 管理 |
| DeepSeek | `DEEPSEEK_API_KEY` | deepseek-chat | [DeepSeek 开放平台](https://platform.deepseek.com/) |

> 推荐使用阿里千问（国内直连，免费额度充足）

## 环境变量配置

### Windows (CMD)
```cmd
set ALI_QWEN_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Windows (PowerShell)
```powershell
$env:ALI_QWEN_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Linux / macOS
```bash
export ALI_QWEN_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 持久化配置

**Windows 系统环境变量：**
1. 打开「系统属性」→「高级」→「环境变量」
2. 新增用户变量：变量名 `ALI_QWEN_API_KEY`，变量值：你的 API Key
3. 重启终端生效

## 命令行参数

| 参数 | 缩写 | 说明 | 默认值 |
|------|------|------|--------|
| `--position` | `-p` | 目标岗位 | 交互输入 |
| `--resume` | `-r` | 简历文本或文件路径 | 交互输入 |
| `--type` | `-t` | 面试类型：技术面/HR面/压力面/群面 | 技术面 |
| `--api` | — | API 提供商：dashscope/deepseek | dashscope |

## 示例

```bash
# 技术面 - 后端开发
python interview_simulator.py -p "后端开发工程师" -r resume.txt -t "技术面"

# HR面 - 产品经理
python interview_simulator.py -p "产品经理" -r resume.txt -t "HR面"

# 压力面 - 使用 DeepSeek API
python interview_simulator.py -p "销售经理" -r resume.txt -t "压力面" --api deepseek
```
