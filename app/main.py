from fastapi import FastAPI

#prueba

from app.config import settings
from app.routes.items import router as items_router

app = FastAPI(title="examen-u3 items API")
app.include_router(items_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": settings.git_sha}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.port)
