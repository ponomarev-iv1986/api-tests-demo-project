from typing import Optional

import allure
import jsonschema
from jsonschema.exceptions import ValidationError
from requests import Response

from api_requests import pprb_request
from helpers.load_json_schema import load_schema


class GetInfoForROA:
    def __init__(self, request: pprb_request.SendRequest):
        self.request = request
        self.response: Optional[Response] = None

    # API_METHODS
    @allure.step('Выполнить запрос GetInfoForROARq')
    def send_request(self, *args, **kwargs):
        self.response = self.request.post('/v1/getInfoForROA', *args, **kwargs)

    # VERIFICATION
    @allure.step('Проверить, что status code ответа равен {status_code}.')
    def verify_status_code(self, status_code):
        actual_status_code = self.response.status_code
        assert actual_status_code == status_code, (
            f'Получен status code = {actual_status_code}. '
            f'Ожидался status code = {status_code}.'
        )

    @allure.step('Проверить, что заголовки ответа соответствуют ожидаемым.')
    def verify_headers(self, key, value):
        # response_headers = self.response.headers
        response_headers = {  # Заглушка, необходимо будет убрать и раскомментировать строчку выше
            'RqUID': 'TBD'
        }
        actual_value = response_headers.get(key)
        assert actual_value == value, (
            f'В заголовке {key} получено значение {actual_value}. '
            f'В заголовке {key} ожидалось значение {value}.'
        )

    @allure.step(
        'Проверить, что структура ответа соответствует ожидаемой JSON схеме.'
    )
    def validate_json_schema(self, json_schema):
        response_body = self.response.json()
        schema = load_schema(json_schema)
        try:
            jsonschema.validate(response_body, schema)
        except ValidationError as err:
            raise AssertionError(
                f'Структура ответа не соответствует ожидаемой JSON схеме.\n\n{err}'
            )

    @allure.step(
        'Проверить, что поле status в теле ответа соответствует ожидаемому.'
    )
    def verify_status(self, **status):
        response_body = self.response.json()
        actual_status = response_body.get('status')
        assert actual_status == status, (
            f'В теле ответа получен status = {actual_status}. '
            f'В теле ответа ожидался status = {status}.'
        )

    @allure.step(
        'Проверить, что поле response/statusProcess в теле ответа соответствует ожидаемому.'
    )
    def verify_status_process_in(self, *status_process):
        response_body = self.response.json()
        # actual_status_process = 'example'
        try:
            actual_status_process = response_body['response']['statusProcess']
        except KeyError:
            actual_status_process = None
        assert actual_status_process in status_process, (
            f'Получен statusProcess = {actual_status_process}. '
            f'Ожидался statusProsess = {", или ".join(status_process)}'
        )

    @allure.step(
        'Проверить, что поле response/statusProcess в теле ответа соответствует ожидаемому.'
    )
    def verify_status_process_not_in(self, *status_process):
        response_body = self.response.json()
        # actual_status_process = 'example'
        try:
            actual_status_process = response_body['response']['statusProcess']
        except KeyError:
            actual_status_process = None
        assert actual_status_process not in status_process, (
            f'Получен statusProcess = {actual_status_process}. '
            f'Ожидался statusProsess != {", или ".join(status_process)}'
        )
