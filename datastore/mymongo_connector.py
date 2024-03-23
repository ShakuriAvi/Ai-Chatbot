from typing import Dict, Any

from bson import ObjectId

from config.cfg import MONGO_SETTINGS
from pymongo.mongo_client import MongoClient


class MongoConnector():
    def __init__(self):
        self.uri = MONGO_SETTINGS["uri"]
        self.db_name = MONGO_SETTINGS["db"]
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]

    def close_conn(self):
        if self.client is not None:
            self.client.close()

    def get_table(self, db_name):
        return self.client.get_database(db_name)

    def get_last_user_conversation(self, user_id: str) -> Dict[str, Any]:
        collection = self.db["users_conversations"]
        # Query MongoDB to find the last conversation of the user
        last_conversation = collection.find_one({'user_id': user_id}, sort=[('_id', -1)])
        return last_conversation

    def update_last_user_conversation(self, conversation_id: str, conversation_data: list) -> bool:
        collection = self.db["users_conversations"]

        # Update the conversation with the given conversation_id
        result = collection.update_one({'_id': ObjectId(conversation_id)},
                                       {'$set': {'conversation': conversation_data}})

        return result.modified_count > 0

    def add_new_user_conversation(self, user_id: str, conversation: list, ai_result: list) -> bool:
        # Create a document to insert into the collection
        collection = self.db["users_conversations"]
        new_conversation = {'user_id': user_id, 'conversation': conversation, 'ai_result': ai_result}
        # Insert the new conversation document into the collection
        result = collection.insert_one(new_conversation)
        return result.inserted_id
