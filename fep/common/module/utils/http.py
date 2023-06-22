import requests

from typing import final


class HTTP:
    """Class that contains HTTP utils"""

    @final
    def http_get(self, *args, **kwargs) -> requests.Response:
        """Perform HTTP get request"""
        return requests.get(*args, **kwargs)

    @final
    def http_post(self, *args, **kwargs) -> requests.Response:
        """Perform HTTP post request"""
        return requests.post(*args, **kwargs)
