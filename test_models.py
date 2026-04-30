import asyncio
from openai import AsyncOpenAI

async def test():
    client = AsyncOpenAI(
        api_key="tp-s6rn3ztxvp0ln1gjmlxo8exq8ebw3lbn7fuxuwxn92jeihqt",
        base_url="https://token-plan-sgp.xiaomimimo.com/v1"
    )
    
    try:
        models = await client.models.list()
        for model in models.data:
            print(model.id)
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

asyncio.run(test())
