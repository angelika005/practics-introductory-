from fastapi import FastAPI


app = FastAPI()


@app.post("/app")
async def handle_request():
    return
