import logging
import allure
import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Session, Response


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        with step(f'{method} {url}'):
            allure.attach(body=curl, name="Request curl", attachment_type=AttachmentType.TEXT, extension='txt')
            return response