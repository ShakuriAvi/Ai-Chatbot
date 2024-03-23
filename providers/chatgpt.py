from providers.provider import Provider
from config.cfg import CHATGPT_SETTINGS

CONTENT_SERVICE = "gpt-3.5-turbo"
MAX_TOKENS = 4096


class ChatGPT(Provider):
    api_url = "https://api.openai.com/v1"  # Updated URL for chat-based models
    def __init__(self):
        self.base_query = CHATGPT_SETTINGS["base_query"]
        self.fix_query = CHATGPT_SETTINGS["fix_query"]
        self.access_token = CHATGPT_SETTINGS["api_key"]


    def get_headers(self):
        """get headers implementation override"""
        return {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}

    def create_new_query(self, **kwargs) -> str:
        CONTENT_URL = "chat/completions"
        user_query = kwargs.get("query")
        ai_results = kwargs.get("ai_results")
        conversation = kwargs.get("last_conversation", "")
        fix_message = kwargs.get("fix_message", False)

        query = None
        if not fix_message:
            query = self.base_query
            query = query.replace("{{ai_results}}", str(ai_results))

        else:
            query = self.fix_query
            query = query.replace("{{conversation}}", str(conversation))
        query = query.replace("{{user_query}}", user_query)
        data = {
            "model": CONTENT_SERVICE,
            "max_tokens": MAX_TOKENS,  # Adjust as needed
            "temperature": 0.0,
            "messages": [{"role": "user", "content": query}],
        }
        params = {"headers": self.get_headers(), "data": data}
        res = self.post(CONTENT_URL, **params)
        if res.status_code != 200:
            raise ValueError(res.text)
        res_obj = res.json()
        chatgpt_answer = res_obj.get("choices")[0]["message"]["content"]
        return chatgpt_answer






