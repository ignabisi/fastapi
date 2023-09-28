from typing import List
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.pydantic import SumaryResopnseSchema, SumaryPayloadSchema
from app.api import crud
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.get("/")
async def read_all_summaries() -> List[SummarySchema]:
    summaries = await crud.get_all()
    if not summaries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No summaries found"
        )
    return summaries


@router.get("/{summary_id}")
async def get_summary(summary_id: int):
    summary = await crud.get(summary_id)
    if not summary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Summary not found"
        )
    return summary


@router.post(
    "/", response_model=SumaryResopnseSchema, status_code=status.HTTP_201_CREATED
)
async def create_summary(payload: SumaryPayloadSchema) -> SumaryResopnseSchema:
    summary_id = await crud.post(payload)
    return JSONResponse(
        content={"id": summary_id, "url": payload.url},
        status_code=status.HTTP_201_CREATED,
    )
