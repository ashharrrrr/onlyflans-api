from fastapi import FastAPI

app = FastAPI(title="OnlyFlans API")


@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}
