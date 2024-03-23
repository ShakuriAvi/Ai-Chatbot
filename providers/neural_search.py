from providers.provider import Provider


class NeuralSearch(Provider):
    api_url = 'http://localhost:8000/api'

    def create_new_query(self, **kwargs) -> list:
        query = kwargs.get('query')
        params = {'q': query}
        response = self.get("search", **params)
        return response["result"]



