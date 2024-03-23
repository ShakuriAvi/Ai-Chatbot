import json
from typing import Dict, Any
import requests
from requests import Response
from abc import ABC, abstractmethod

class Provider(ABC):
    _uri_format = "{0}/{1}"
    api_url = "INVALID_URL"

    def get(self, *args, **kwargs) -> Response:
        """Generic GET implementation - In case there is a need for a specific implementation, override this"""
        endpoint = args[0]
        if not endpoint:
            raise ValueError
        uri = self._uri_format.format(self.api_url, endpoint)
        res = requests.get(uri, params=kwargs)
        if res.status_code != 200:
            raise ValueError(f"")
        return json.loads(res.text)

    def post(self, *args, **kwargs) -> Response:
        """Generic GET implementation - In case there is a need for a specific implementation, override this"""
        endpoint = args[0]
        if not endpoint:
            raise ValueError
        uri = self._uri_format.format(self.api_url, endpoint)
        data = kwargs.get("data")
        headers = kwargs.get("headers")

        res = requests.post(uri, headers=headers, json=data)
        return res

    @abstractmethod
    def create_new_query(self, **kwargs):
        pass