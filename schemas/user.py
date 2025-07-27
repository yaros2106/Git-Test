from uuid import UUID

from pydantic import BaseModel, StringConstraints
from typing import Annotated


class UserSchema(BaseModel):
    id: UUID
    name: Annotated[
        str,
        StringConstraints(min_length=3, max_length=32),
    ]
