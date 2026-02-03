from fastapi import FastAPI
from src.api.routes import bills, dashboard

app = FastAPI(
    title="Gerenciador de contas",
    version="1.0.0"
)

app.include_router(bills.router)
app.include_router(dashboard.router)