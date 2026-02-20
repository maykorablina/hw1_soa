from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Marketplace API", version="1.0.0")


@app.get("/health")
def health_check():
    return JSONResponse(
        content={"status": "OK", "service": "api-gateway"},
        status_code=200,
    )


@app.get("/")
def root():
    return JSONResponse(
        content={"message": "Marketplace API is running. /health to check status."},
        status_code=200,
    )
