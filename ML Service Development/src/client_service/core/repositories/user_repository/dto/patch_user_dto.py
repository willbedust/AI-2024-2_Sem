from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PatchUserDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    password: Optional[str] = Field(None, max_length=50)
    funds: Optional[float] = Field(None)
