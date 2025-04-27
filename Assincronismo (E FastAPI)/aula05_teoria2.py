from fastapi import FastAPI
import uvicorn
import asyncio

# nesse script o caso é assincrono com o fastAPI

app = FastAPI()

@app.get('/')
async def ola_mundo():
    await asyncio.sleep(20)
    return { 'olá': 'mundo!' }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1) # essa linha já faz o "trabalho" do asyncio.run()
