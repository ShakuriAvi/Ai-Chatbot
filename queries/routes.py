from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from loguru import logger
from .logic import QueryActionsLogic
from .models import Query
from .exceptions import type_unsupported
queries_actions = APIRouter()


@queries_actions.post("/query")
async def create_query(
        new_query: Query,
        action_logic: QueryActionsLogic = Depends(QueryActionsLogic)):
    if not (isinstance(new_query.user_id, str) and isinstance(new_query.message, str)):
        raise type_unsupported
    logger.info(f"User {new_query.user_id} has requested with new query: {new_query.message}")
    response = await action_logic.query_manager(new_query)

    return {"answer": response}
