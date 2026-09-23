# local-agent

用 Python 调用本地 [Ollama](https://ollama.com) 模型的最小 Agent 工程骨架。

## 要求

- Python 3.8+
- 本机已安装并运行 Ollama
- 已拉取模型，例如：`ollama pull llama3.2`

## 安装

```powershell
cd D:\work\remote\local-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 运行

```powershell
# 可选：指定模型
$env:OLLAMA_MODEL = "llama3.2"
python main.py
python main.py 你好，请简短回复
```

## 目录

| 路径 | 说明 |
|---|---|
| `main.py` | CLI 入口 |
| `src/ollama_client.py` | `/api/tags`、`/api/chat` 封装 |
| `config/` | 环境变量示例 |
| `tests/` | 占位测试 |
| `docs/` | 文档 |
| `scripts/` | 辅助脚本 |
| `requirements.txt` | 依赖 |
| `LICENSE` | Apache-2.0 |

## License

Apache License 2.0. 见 [LICENSE](./LICENSE)。
