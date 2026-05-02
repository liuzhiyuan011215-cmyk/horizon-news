import asyncio
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.models import Config
from src.services.webhook import WebhookNotifier

async def test_webhook_notification():
    # 加载配置
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        import json
        config_data = json.load(f)
    
    config = Config(**config_data)
    
    if not config.webhook:
        print("Webhook not configured")
        return
    
    print(f"Webhook enabled: {config.webhook.enabled}")
    print(f"Webhook URL env: {config.webhook.url_env}")
    
    # 检查环境变量
    url = os.getenv(config.webhook.url_env or "")
    print(f"Webhook URL: {url}")
    
    if not url:
        print(f"Environment variable {config.webhook.url_env} not set")
        return
    
    # 创建webhook notifier
    notifier = WebhookNotifier(config.webhook)
    
    # 测试发送
    summary = "🌅 Horizon新闻雷达测试\n\n这是一条测试消息，说明webhook配置正确。"
    
    variables = {
        "date": "2026-05-02",
        "language": "zh",
        "important_items": 3,
        "all_items": 10,
        "result": "success",
        "timestamp": "1777712072",
        "message_title": "Horizon 2026-05-02 日报",
        "message_kind": "summary",
        "summary": summary,
    }
    
    print("Sending webhook notification...")
    await notifier.notify(variables)
    print("Webhook notification sent!")

if __name__ == "__main__":
    asyncio.run(test_webhook_notification())
