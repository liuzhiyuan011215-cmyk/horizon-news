import asyncio
import httpx
import json

async def test_webhook():
    url = "https://api.telegram.org/bot8607025223:AAFZo693pYIQAKZ8nA6zrveb5UhYl2cZDEI/sendMessage"
    body = {
        "chat_id": "6760290103",
        "text": "🌅 Horizon新闻雷达测试\n\n这是一条测试消息，说明webhook配置正确。\n\n明天早上8点你将收到每日科技新闻速递。",
        "parse_mode": "Markdown"
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=body)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")

asyncio.run(test_webhook())
