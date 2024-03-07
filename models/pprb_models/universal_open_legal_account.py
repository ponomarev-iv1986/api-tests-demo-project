from typing import Optional

import allure
import jsonschema
from jsonschema.exceptions import ValidationError
from requests import Response

from api_requests import pprb_request
from helpers.load_json_schema import load_schema


class UniversalOpenLegalAccount:
    def __init__(self, request: pprb_request.SendRequest):
        self.request = request
        self.response_identification: Optional[Response] = None
        self.response_generate_doc: Optional[Response] = None
        self.response_open_account: Optional[Response] = None

    # API_METHODS
    @allure.step('Выполнить запрос identificationULOpenRq')
    def send_identification(self, *args, **kwargs):
        self.response_identification = self.request.post(
            '/oip-rko-scripts/universalOpenLegalAccount/v1/universalOpenLegalAccount',
            *args,
            **kwargs,
        )

    @allure.step('Выполнить запрос generateDocumentClientOpenRq')
    def send_generate_doc(self, *args, **kwargs):
        self.response_generate_doc = self.request.post(
            '/oip-rko-scripts/universalOpenLegalAccount/v1/universalOpenLegalAccount',
            *args,
            **kwargs,
        )

    @allure.step('Выполнить запрос openAccountRq')
    def send_open_account(self, *args, **kwargs):
        self.response_open_account = self.request.post(
            '/oip-rko-scripts/universalOpenLegalAccount/v1/universalOpenLegalAccount',
            *args,
            **kwargs,
        )

    # VERIFICATION_IDENTIFICATION
    @allure.step(
        'Проверить, что status code ответа identificationULOpenRs'
        ' равен {status_code}.'
    )
    def verify_identification_status_code(self, status_code):
        actual_status_code = self.response_identification.status_code
        assert actual_status_code == status_code, (
            f'Получен status code = {actual_status_code}. '
            f'Ожидался status code = {status_code}.'
        )

    @allure.step(
        'Проверить, что заголовки ответа identificationULOpenRs'
        ' соответствуют ожидаемым.'
    )
    def verify_identification_headers(self, key, value):
        response_headers = self.response_identification.headers
        actual_value = response_headers.get(key)
        assert actual_value == value, (
            f'В заголовке {key} получено значение {actual_value}. '
            f'В заголовке {key} ожидалось значение {value}.'
        )

    @allure.step(
        'Проверить, что структура ответа identificationULOpenRs'
        ' соответствует ожидаемой JSON схеме.'
    )
    def validate_identification_json_schema(self, json_schema):
        response_body = self.response_identification.json()
        schema = load_schema(json_schema)
        try:
            jsonschema.validate(response_body, schema)
        except ValidationError as err:
            raise AssertionError(
                f'Структура ответа не соответствует ожидаемой JSON схеме.\n\n{err}'
            )

    # VERIFICATION_GENERATE_DOC
    @allure.step(
        'Проверить, что status code ответа generateDocumentClientOpenRs'
        ' равен {status_code}.'
    )
    def verify_generate_doc_status_code(self, status_code):
        actual_status_code = self.response_generate_doc.status_code
        assert actual_status_code == status_code, (
            f'Получен status code = {actual_status_code}. '
            f'Ожидался status code = {status_code}.'
        )

    @allure.step(
        'Проверить, что заголовки ответа generateDocumentClientOpenRs'
        ' соответствуют ожидаемым.'
    )
    def verify_generate_doc_headers(self, key, value):
        response_headers = self.response_generate_doc.headers
        actual_value = response_headers.get(key)
        assert actual_value == value, (
            f'В заголовке {key} получено значение {actual_value}. '
            f'В заголовке {key} ожидалось значение {value}.'
        )

    @allure.step(
        'Проверить, что структура ответа generateDocumentClientOpenRs'
        ' соответствует ожидаемой JSON схеме.'
    )
    def validate_generate_doc_json_schema(self, json_schema):
        response_body = self.response_generate_doc.json()
        schema = load_schema(json_schema)
        try:
            jsonschema.validate(response_body, schema)
        except ValidationError as err:
            raise AssertionError(
                f'Структура ответа не соответствует ожидаемой JSON схеме.\n\n{err}'
            )

    # VERIFICATION_OPEN_ACCOUNT
    @allure.step(
        'Проверить, что status code ответа openAccountRq'
        ' равен {status_code}.'
    )
    def verify_open_account_status_code(self, status_code):
        actual_status_code = self.response_open_account.status_code
        assert actual_status_code == status_code, (
            f'Получен status code = {actual_status_code}. '
            f'Ожидался status code = {status_code}.'
        )

    @allure.step(
        'Проверить, что заголовки ответа openAccountRq'
        ' соответствуют ожидаемым.'
    )
    def verify_open_account_headers(self, key, value):
        response_headers = self.response_open_account.headers
        actual_value = response_headers.get(key)
        assert actual_value == value, (
            f'В заголовке {key} получено значение {actual_value}. '
            f'В заголовке {key} ожидалось значение {value}.'
        )

    @allure.step(
        'Проверить, что структура ответа openAccountRq'
        ' соответствует ожидаемой JSON схеме.'
    )
    def validate_open_account_json_schema(self, json_schema):
        response_body = self.response_open_account.json()
        schema = load_schema(json_schema)
        try:
            jsonschema.validate(response_body, schema)
        except ValidationError as err:
            raise AssertionError(
                f'Структура ответа не соответствует ожидаемой JSON схеме.\n\n{err}'
            )
