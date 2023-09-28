from pydantic import BaseModel


class SumaryPayloadSchema(BaseModel):
    url: str


class SumaryResopnseSchema(SumaryPayloadSchema):
    id: int
