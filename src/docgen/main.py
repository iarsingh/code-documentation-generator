from docgen.ops import router as ops_router
from fastapi import FastAPI, HTTPException
from docgen.extract import extract

app = FastAPI()
app.include_router(ops_router, prefix="/v1")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/extract")
def post_extract(body: dict):
    try:
        return extract(body.get("text", ""))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
