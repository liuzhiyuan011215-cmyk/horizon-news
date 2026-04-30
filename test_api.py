import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

async def test():
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"API Key: {api_key[:10]}...")
    
    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://token-plan-sgp.xiaomimimo.com/v1"
    )
    
    try:
        response = await client.chat.completions.create(
            model="mimo-2.5-pro",
            messages=[
                {"role": "system", "content": "你是一个助手"},
                {"role": "user", "content": "你好，请回复OK"}
            ],
            temperature=0.3,
            max_tokens=100
        )
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

asyncio.run(test())
