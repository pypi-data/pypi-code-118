from python_helper import EnvironmentHelper
from python_framework.api.src.enumeration.HttpStatus import HttpStatus
from python_framework.api.src.util import Serializer
from python_framework.api.src.service.flask.FlaskManager import Controller, ControllerMethod

import ClientTestDto


BASE_CONTROLLER_URL = f'/exception/test/{EnvironmentHelper.get("URL_VARIANT")}'
GET_TEST = 'get'
GET_TEST_URL = f'/{GET_TEST}'
POST_TEST = 'post'
POST_TEST_URL = f'/{POST_TEST}'
PUT_TEST = 'put'
PUT_TEST_URL = f'/{PUT_TEST}'
PATCH_TEST = 'patch'
PATCH_TEST_URL = f'/{PATCH_TEST}'
DELETE_TEST = 'delete'
DELETE_TEST_URL = f'/{DELETE_TEST}'


@Controller(url=f'{BASE_CONTROLLER_URL}/<string:urlParam>/<string:otherUrlParam>', tag='ClientTestController', description='Client Controller test')
class ClientExceptionTestController:

    @ControllerMethod(
        url = GET_TEST_URL,
        requestHeaderClass = [ClientTestDto.ClientTestRequestHeaderDto],
        requestParamClass = [ClientTestDto.ClientTestRequestParamDto],
        responseClass = ClientTestDto.ClientTestResponseDto,
        logRequest = True,
        logResponse = True
    )
    def get(self, urlParam=None, otherUrlParam=None, params=None, headers=None):
        return self.globals.api.resource.client.exceptionTest.getMethod(
            f'/{urlParam}/{otherUrlParam}{GET_TEST_URL}/all',
            headers = headers,
            params = params
        )[0], {GET_TEST: f'headers-{GET_TEST}'}, HttpStatus.OK

    @ControllerMethod(
        url = POST_TEST_URL,
        requestHeaderClass = ClientTestDto.ClientTestRequestHeaderDto,
        requestParamClass = ClientTestDto.ClientTestRequestParamDto,
        requestClass = ClientTestDto.ClientTestRequestDto,
        responseClass = ClientTestDto.ClientTestResponseDto,
        logRequest = True,
        logResponse = True
    )
    def post(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        return self.globals.api.resource.client.exceptionTest.postMethod(
            f'/{urlParam}/{otherUrlParam}{POST_TEST_URL}/all',
            dto,
            headers = headers,
            params = params
        )[0], {POST_TEST: f'headers-{POST_TEST}'}, HttpStatus.OK

    @ControllerMethod(
        url = PUT_TEST_URL,
        requestHeaderClass = ClientTestDto.ClientTestRequestHeaderDto,
        requestParamClass = ClientTestDto.ClientTestRequestParamDto,
        requestClass = ClientTestDto.ClientTestRequestDto,
        responseClass = ClientTestDto.ClientTestResponseDto,
        logRequest = True,
        logResponse = True
    )
    def put(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        return self.globals.api.resource.client.exceptionTest.putMethod(
            f'/{urlParam}/{otherUrlParam}{PUT_TEST_URL}/all',
            dto,
            headers = headers,
            params = params
        )[0], {PUT_TEST: f'headers-{PUT_TEST}'}, HttpStatus.OK

    @ControllerMethod(
        url = PATCH_TEST_URL,
        requestHeaderClass = ClientTestDto.ClientTestRequestHeaderDto,
        requestParamClass = ClientTestDto.ClientTestRequestParamDto,
        requestClass = ClientTestDto.ClientTestRequestDto,
        responseClass = ClientTestDto.ClientTestResponseDto,
        logRequest = True,
        logResponse = True
    )
    def patch(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        return self.globals.api.resource.client.exceptionTest.patchMethod(
            f'/{urlParam}/{otherUrlParam}{PATCH_TEST_URL}/all',
            dto,
            headers = headers,
            params = params
        )[0], {PATCH_TEST: f'headers-{PATCH_TEST}'}, HttpStatus.OK

    @ControllerMethod(
        url = DELETE_TEST_URL,
        requestHeaderClass = ClientTestDto.ClientTestRequestHeaderDto,
        requestParamClass = ClientTestDto.ClientTestRequestParamDto,
        requestClass = ClientTestDto.ClientTestRequestDto,
        responseClass = ClientTestDto.ClientTestResponseDto,
        logRequest = True,
        logResponse = True
    )
    def delete(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        return self.globals.api.resource.client.exceptionTest.deleteMethod(
            f'/{urlParam}/{otherUrlParam}{DELETE_TEST_URL}/all',
            dto,
            headers = headers,
            params = params
        )[0], {DELETE_TEST: f'headers-{DELETE_TEST}'}, HttpStatus.OK


@Controller(url=f'{BASE_CONTROLLER_URL}', tag='ClientTestController', description='Client Controller test')
class ClientExceptionTestBatchController:

    @ControllerMethod(
        url = f'/<string:urlParam>/<string:otherUrlParam>{GET_TEST_URL}/all',
        requestHeaderClass = [ClientTestDto.ClientTestRequestHeaderDto],
        requestParamClass = [ClientTestDto.ClientTestRequestParamDto],
        responseClass = [[ClientTestDto.ClientTestResponseDto]],
        logRequest = True,
        logResponse = True
    )
    def get(self, urlParam=None, otherUrlParam=None, params=None, headers=None):
        raise Exception("Some unexpected exception")

    @ControllerMethod(
        url = f'/<string:urlParam>/<string:otherUrlParam>{POST_TEST_URL}/all',
        requestHeaderClass = [ClientTestDto.ClientTestRequestHeaderDto],
        requestParamClass = [ClientTestDto.ClientTestRequestParamDto],
        requestClass = [ClientTestDto.ClientTestRequestDto],
        responseClass = [[ClientTestDto.ClientTestResponseDto]],
        logRequest = True,
        logResponse = True
    )
    def post(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        raise Exception("Some unexpected exception")

    @ControllerMethod(
        url = f'/<string:urlParam>/<string:otherUrlParam>{PUT_TEST_URL}/all',
        requestHeaderClass = [ClientTestDto.ClientTestRequestHeaderDto],
        requestParamClass = [ClientTestDto.ClientTestRequestParamDto],
        requestClass = [ClientTestDto.ClientTestRequestDto],
        responseClass = [[ClientTestDto.ClientTestResponseDto]],
        logRequest = True,
        logResponse = True
    )
    def put(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        raise Exception("Some unexpected exception")

    @ControllerMethod(
        url = f'/<string:urlParam>/<string:otherUrlParam>{PATCH_TEST_URL}/all',
        requestHeaderClass = [ClientTestDto.ClientTestRequestHeaderDto],
        requestParamClass = [ClientTestDto.ClientTestRequestParamDto],
        requestClass = [ClientTestDto.ClientTestRequestDto],
        responseClass = [[ClientTestDto.ClientTestResponseDto]],
        logRequest = True,
        logResponse = True
    )
    def patch(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        raise Exception("Some unexpected exception")

    @ControllerMethod(
        url = f'/<string:urlParam>/<string:otherUrlParam>{DELETE_TEST_URL}/all',
        requestHeaderClass = [ClientTestDto.ClientTestRequestHeaderDto],
        requestParamClass = [ClientTestDto.ClientTestRequestParamDto],
        requestClass = [ClientTestDto.ClientTestRequestDto],
        responseClass = [[ClientTestDto.ClientTestResponseDto]],
        logRequest = True,
        logResponse = True
    )
    def delete(self, dto, urlParam=None, otherUrlParam=None, params=None, headers=None):
        raise Exception("Some unexpected exception")
