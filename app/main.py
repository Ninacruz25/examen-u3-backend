from fastapi import FastAPI

from app.routes.items import router as items_router

app = FastAPI(title="examen-u3 items API")
app.include_router(items_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    from app.config import settings

    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.port)
