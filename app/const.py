from enum import Enum
from typing import (
    Final,
    List,
)

from fastapi.security import APIKeyHeader

AUTH_TAGS: Final[List[str | Enum] | None] = ["Authentication"]
USER_TAGS: Final[List[str | Enum] | None] = ["User"]
TABLE_TAGS: Final[List[str | Enum] | None] = ["Table"]
LOG_TAGS: Final[List[str | Enum] | None] = ["Log"]
AUTH_URL: Final = "/token"

TOKEN_EXPIRE_MINUTES: Final = 60

TOKEN_ALGORITHM: Final = "HS256"

apikey_scheme = APIKeyHeader(name="Authorization")
