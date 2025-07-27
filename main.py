from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get(
    "/",
    response_class=HTMLResponse,
)
def root() -> str:
    return "<h1>Hello yaros</h1>"
