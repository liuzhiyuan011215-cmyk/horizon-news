import asyncio
import httpx
import json

async def test_horizon_webhook():
    # 模拟Horizon的webhook调用
    url = "https://api.telegram.org/bot8607025223:AAFZo693pYIQAKZ8nA6zrveb5UhYl2cZDEI/sendMessage"
    
    # 模拟Horizon生成的summary
    summary = """🌅 Horizon 每日科技新闻速递 - 2026-05-02

🤖 科技新闻

1. **AI技术突破** ⭐️ 8/10
   - 最新的AI技术取得了重大突破，将改变多个行业

2. **开源项目更新** ⭐️ 7/10
   - 多个热门开源项目发布了新版本

3. **科技公司动态** ⭐️ 6/10
   - 各大科技公司发布了新的产品和服务"""
    
    body = {
        "chat_id": "6760290103",
        "text": summary,
        "parse_mode": "Markdown"
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=body)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")

asyncio.run(test_horizon_webhook())
