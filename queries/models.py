from pydantic import BaseModel
class Query(BaseModel):
    user_id: str
    message: str
