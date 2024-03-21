from abc import ABC, abstractmethod


class BaseClientAPI(ABC):
    """Base Client for requested data from API"""

    @property
    def base_url(self):
        return ''

    @abstractmethod
    def get_path_of_url(self, *args, **kwargs) -> None:
        """Abstract method for getting path of API url"""
        pass

    @abstractmethod
    async def from_api(self, *args, **kwargs) -> None:
        """Abstract method for request and get data from API"""
        pass
