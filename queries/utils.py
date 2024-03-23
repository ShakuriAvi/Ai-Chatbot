from providers.chatgpt import ChatGPT
from providers.neural_search import NeuralSearch
from providers.provider import Provider


class ProviderContext:
    def __init__(self, strategy: Provider):
        self._strategy = strategy

    def set_strategy(self, strategy: Provider):
        self._strategy = strategy

    def execute_query(self, **kwargs):
        return self._strategy.create_new_query(**kwargs)


def chatgpt_manager(**kwargs) -> str:
    chatgpt_strategy: ChatGPT = ChatGPT()
    chatgpt_context = ProviderContext(chatgpt_strategy)
    res = chatgpt_context.execute_query(**kwargs)
    return res


def neural_manager(**kwargs) -> list:
    query = kwargs.get("query")
    neural_search: NeuralSearch = NeuralSearch()
    neural_context = ProviderContext(neural_search)
    res = neural_context.execute_query(query=query)
    return res
