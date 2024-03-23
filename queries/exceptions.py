from fastapi import HTTPException
from fastapi import status

answer_not_exists_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="As of my last update in January 2022, I don't have the data about your question."
)
type_unsupported = HTTPException(
    status_code=status.WS_1003_UNSUPPORTED_DATA, detail="one of params is invalid"
)
