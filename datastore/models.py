from datetime import datetime
from typing import Any
from typing import Dict

from pydantic import BaseModel


class EndpointLog(BaseModel):
    data_date: datetime
    endpoint: str
    username: str
    params: Dict[str, Any]
