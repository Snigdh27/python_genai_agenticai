import asyncio
import aiohttp

async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D"]*3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())