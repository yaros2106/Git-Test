from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get(
    "/",
    response_class=HTMLResponse,
)
def root(
    name: str = "World",
) -> str:
    return f"<h1>Hello {name}</h1>"
