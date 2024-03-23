from typing import Any
from queries.models import Query
from datastore.mymongo_connector import MongoConnector
import queries.utils as utils
from queries.exceptions import answer_not_exists_exception


class QueryActionsLogic:
    def __init__(self):
        self._database_connector = MongoConnector()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._database_connector.close_conn()

    async def query_manager(self, query: Query) -> str:
        last_user_messages = self.__get_last_conversation(query.user_id)
        if len(last_user_messages) > 0:
            res = self.__continue_old_conversation(last_user_messages, query)
        else:
            res = self.__start_new_conversation(query)

        return res

    def __start_new_conversation(self, query: Query) -> str:
        ai_res = utils.neural_manager(query=query.message)
        if len(ai_res) == 0:
            raise answer_not_exists_exception()
        chatbot_res = utils.chatgpt_manager(ai_results=ai_res, query=query.message)
        if not self.__exist_data_for_the_query(chatbot_res):
            raise answer_not_exists_exception
        new_conversation = [{"ai_answer": ai_res, "user_query": query.message, "chatbot_answer": chatbot_res}]
        self.__add_conversation(query.user_id, new_conversation, ai_res)
        return chatbot_res

    def __continue_old_conversation(self, last_user_messages, query):
        last_conversation = last_user_messages["conversation"]
        ai_res = last_user_messages["ai_result"]
        chatbot_res = utils.chatgpt_manager(ai_results=ai_res, query=query.message)
        if not self.__exist_data_for_the_query(chatbot_res):
            chatbot_res = utils.chatgpt_manager(ai_results=ai_res,
                                                last_conversation=[query["user_query"] for query in last_conversation],
                                                query=query.message, fix_message=True)
            query.message = chatbot_res
            chatbot_res = self.__start_new_conversation(query)
        else:
            new_conversation = {"user_query": query.message, "chatbot_answer": chatbot_res}
            last_conversation.append(new_conversation)
            self.__update_last_conversation(last_user_messages["_id"], last_conversation)
        return chatbot_res

    def __exist_data_for_the_query(self, chatbot_res):
        if "Nullable" in chatbot_res:
            return False
        return True

    def __get_last_conversation(self, user_id: str) -> Any:  # todo
        conversation_response = self._database_connector.get_last_user_conversation(user_id)
        last_answer = conversation_response if conversation_response else []
        return last_answer

    def __update_last_conversation(self, conversation_id: str, conversation: list) -> bool:
        conversation_response = self._database_connector.update_last_user_conversation(conversation_id, conversation)
        return conversation_response

    def __add_conversation(self, user_id: str, conversation: list, ai_result) -> int:
        conversation_response = self._database_connector.add_new_user_conversation(user_id, conversation, ai_result)
        return conversation_response
