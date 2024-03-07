import json

import allure
import curlify
import requests
from allure_commons.types import AttachmentType

import config


class SendRequest(requests.Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs):
        response = super().request(
            method=method, url=f'{self.base_url}{url}', *args, **kwargs
        )
        with allure.step(f'{method} {url}'):
            curl = curlify.to_curl(response.request)
            allure.attach(
                body=curl.encode('utf8'),
                name='CURL запроса',
                attachment_type=AttachmentType.TEXT,
                extension='txt',
            )
            allure.attach(
                body=str(response.status_code),
                name='Response статус-код ответа',
                attachment_type=AttachmentType.TEXT,
                extension='txt',
            )
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=2).encode('utf8'),
                    name='Тело ответа',
                    attachment_type=AttachmentType.JSON,
                    extension='json',
                )
            except requests.exceptions.JSONDecodeError:
                allure.attach(
                    body=response.text,
                    name='Тело ответа',
                    attachment_type=AttachmentType.TEXT,
                    extension='txt',
                )

        return response


send = SendRequest(config.settings.BASE_URL)
send_uola = SendRequest(config.settings.UOLA_URL)
