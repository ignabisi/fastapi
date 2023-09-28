import os
import logging

from fastapi import FastAPI

from app.api.ping import router as ping_router
from app.api.summaries import router as summaries_router
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(ping_router)
    application.include_router(
        summaries_router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_app()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
