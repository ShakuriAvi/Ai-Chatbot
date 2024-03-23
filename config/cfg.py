ENVIRONMENT = "local"

MONGO_SETTINGS = {
    "uri": f"mongodb://localhost:27017/",
    "db": "AIChatBot",
}
CHATGPT_SETTINGS = {
    "api_key": "<API-KEY>",
    "base_query": "Given the answer \"{{ai_results}}\" of my ai and the question \"{{user_query}}\" of my user, please determine"
                  "if the answer is related to the question"
                  "If an answer is found in the output, please formulate a response based on that answer to user."
                  "If no, please return: Nullable.",
    "fix_query": "This is the converstation that my used had with AI: \"{{conversation}}\", "
                 "Based on the following new question: \"{{user_query}}\", "
                 "In case the new question is not related to the rest of the converstation,"
                 " return the new question without any modification."
                 "If the new question does relate to the converstation, "
                 "rephrase the new question to fit the conversation."

}
