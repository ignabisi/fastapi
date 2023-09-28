from typing import Union

from app.models.pydantic import SumaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SumaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> Union[list, None]:
    summaries = await TextSummary.all().values()
    if summaries:
        return summaries
    return None
