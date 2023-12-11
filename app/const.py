from enum import Enum
from typing import (
    Final,
    List,
)

from fastapi.security import APIKeyCookie
from fastapi.security import APIKeyHeader

AUTH_TAGS: Final[List[str | Enum] | None] = ["Authentication"]
USER_TAGS: Final[List[str | Enum] | None] = ["User"]
TABLE_TAGS: Final[List[str | Enum] | None] = ["Table"]
LOG_TAGS: Final[List[str | Enum] | None] = ["Log"]
DATA_TAGS: Final[List[str | Enum] | None] = ["Data"]
AUTH_URL: Final = "/token"

TOKEN_EXPIRE_MINUTES: Final = 60

TOKEN_ALGORITHM: Final = "HS256"

apikey_scheme_page = APIKeyCookie(name="Authorization")
apikey_scheme_request = APIKeyHeader(name="Authorization")
