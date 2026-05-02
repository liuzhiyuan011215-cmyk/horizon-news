import asyncio
import httpx
import json
import os

async def test():
    url = "https://api.telegram.org/bot8607025223:AAFZo693pYIQAKZ8nA6zrveb5UhYl2cZDEI/sendMessage"
    chat_id = "6760290103"
    text = "🌅 Horizon测试\n\n这是一条测试消息"
    
    body = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=body)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")

asyncio.run(test())
