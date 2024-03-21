import aiohttp

from base.client import BaseClientAPI
from base.exceptions import ServerError


class SenderMessageTgAPI(BaseClientAPI):
    """Sender Message API Client"""

    def __init__(self, bot_token: str):
        self._bot_token = bot_token

    @property
    def path(self) -> str:
        """
        Generate path of sending message api url
        :return path of Telegram endpoints to send message
        """
        bot_path = f'bot{self._bot_token}'
        return f'{bot_path}/sendMessage'

    @property
    def base_url(self) -> str:
        """
        Generate base url of api
        :return: base url of api
        """
        return 'https://api.telegram.org/'

    def get_path_of_url(self, *args, **kwargs) -> str:
        """
        Get path of absolute url to request to api
        :return: absolute url
        """
        return self.base_url + self.path

    async def from_api(self, data: dict, *args, **kwargs):
        """Async request to api and validate response"""
        absolute_url = self.get_path_of_url()
        async with aiohttp.ClientSession() as session:
            async with session.post(url=absolute_url, data=data) as response:
                response_data = await response.json()
                if response.status >= 400:
                    raise ServerError('Something went wrong')
                return response_data
