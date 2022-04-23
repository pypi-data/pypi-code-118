import typing as t
import requests

from inspect import currentframe as cf


from .exceptions import *
from .helpers import CurrenciesIDs, MarketsIDs


__all__ = [
    'Bitpin',
]


class Bitpin:
    def __init__(self, api_key: t.Optional[str] = None, api_secret: t.Optional[str] = None,
                 requests_params: t.Optional[t.Dict] = None):
        """
        Initialize the Bitpin SDK .

        :param api_key: API Key (optional)
        :type api_key: str

        :param api_secret: API Secret (optional)
        :type api_secret: str

        :param requests_params: Requests parameters (optional)
        :type requests_params: dict
        """

        self.api_key = api_key
        self.api_secret = api_secret

        self.__access_token = None
        self.__refresh_token = None

        self.__headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        self.__base_url = 'https://api.bitpin.ir'

        # set timeout from requests_params
        if requests_params is not None:
            self.__timeout = requests_params.get('timeout') or 10
            self.__verify = requests_params.get('verify') or None
        else:
            self.__timeout = 10
            self.__verify = True

        self.__handle_access_token()

        return

    def __handle_access_token(self) -> t.Tuple[str, str]:
        """
        Handle access token.
        """

        if self.api_key is not None and self.api_secret is not None:
            login = self.login(self.api_key, self.api_secret)
            self.__access_token = login['access']
            self.__refresh_token = login['refresh']

        return self.__access_token, self.__refresh_token

    @staticmethod
    def __get_func_args(all_locals: t.Dict, remove_keys=None) -> t.Dict:
        """
        Get function arguments.

        :param all_locals: All locals
        :type all_locals: dict

        :return: Function arguments
        :rtype: dict
        """

        if remove_keys is None:
            remove_keys = ['self']

        if 'self' not in remove_keys:
            remove_keys.append('self')

        for i in remove_keys:
            try:
                all_locals.pop(i)
            except KeyError:
                pass

        return all_locals

    def __make_headers(self, func_name: str, auth: t.Optional[bool] = True) -> t.Dict:
        """
        Make headers.

        :param func_name: Function name
        :type func_name: str

        :param auth: Authorization (optional)
        :type auth: bool

        :return: Headers
        :rtype: dict
        """

        f_args = self.__get_func_args(locals())

        headers = self.__headers.copy()

        if auth is True:
            if self.__access_token is None:
                raise InvalidToken(
                    func_name,
                    'access_token is None',
                    f_args=f_args
                )
            headers.update({
                'Authorization': f'Bearer {self.__access_token}'
            })

        return headers

    def _raise_for_exception(
            self,
            func_name: str,
            response: requests.Response,
            additional: t.Dict = None
    ) -> None:
        """
        Check response for exceptions.

        :param response: Response
        :type response: requests.Response

        :param func_name: Function name
        :type func_name: str

        :raises: NobitexAPIException

        :return: None
        :rtype: None
        """

        additional.update(self.__get_func_args(locals()))

        if 200 <= response.status_code < 300:
            try:
                r_json: t.Dict = response.json()
            except Exception as e:
                raise JSONDecodingError(func_name, e, additional)

        else:
            raise StatusCodeError(
                func_name,
                f'invalid status code',
                url=response.url,
                status_code=response.status_code,
                additional=additional
            )

    def _process_response(
            self,
            func_name: str,
            response: requests.Response,
            additional: t.Dict = None,
    ) -> t.Dict:
        """
        Process the response from the Nobitex API.

        :param response: Response
        :type response: requests.Response

        :param func_name: Function name
        :type func_name: str

        :param additional: Arguments (optional)
        :type additional: dict

        :raises: NobitexAPIException

        :return: Response
        :rtype: dict
        """

        self._raise_for_exception(func_name, response, additional)
        return response.json()

    def __request(
            self, method: str, url: str, headers: t.Dict = None,
            params: t.Dict = None, data: t.Dict = None, json_data: t.Dict = None, additional_kwargs: t.Dict = None
    ) -> requests.Response:
        """
        Send request to the Bitpin API.

        :param method: Method
        :type method: str

        :param url: URL
        :type url: str

        :param headers: Headers (optional)
        :type headers: dict

        :param params: Parameters (optional)
        :type params: dict

        :param data: Data (optional)
        :type data: dict

        :param json_data: JSON data (optional)
        :type json_data: dict

        :raises: BitpinAPIException

        :return: Response
        :rtype: requests.Response
        """

        f_name = cf().f_code.co_name

        try:
            response = requests.request(
                method,
                self.__base_url + url,
                headers=headers,
                params=params,
                json=json_data,
                data=data,
                timeout=self.__timeout
            )

            return response
        except Exception as e:
            raise RequestsExceptions(f_name, e, additional_data=additional_kwargs)

    def _request(
            self, func_name: str, method: str, url: str, auth: bool = False,
            params: t.Dict = None, data: t.Dict = None, json_data: t.Dict = None,
    ) -> requests.Response:
        """
        Make a request to the Bitpin API.

        :param method: HTTP method
        :type method: str

        :param url: URL
        :type url: str

        :param auth: Whether to use authentication (optional)
        :type auth: bool

        :param params: Query parameters (optional)
        :type params: dict

        :param data: Request body (optional)
        :type data: dict

        :param json_data: Request body (optional)
        :type json_data: dict

        :param func_name: Function name
        :type func_name: str

        :return: Response
        :rtype: requests.Response
        """

        f_args = self.__get_func_args(locals())

        headers = self.__make_headers(func_name, auth)

        if method.upper() == 'GET':
            return self.__request('GET', url, headers, params, data, json_data)
        elif method.upper() == 'POST':
            return self.__request('POST', url, headers, params, data, json_data)
        else:
            raise RequestsExceptions(
                func_name,
                'Invalid method',
                f_args=f_args
            )

    def set_token(self, token: str):
        """
        Set new fresh token

        :param token: str
        :return: None
        """

        self.__access_token = token

    def login(self, api_key: str, secret_key: str) -> t.Dict:
        """
        Get token.

        :return: Refresh token and access token
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = '/v1/usr/api/login/'

        json_data = {
            'api_key': api_key,
            'secret_key': secret_key,
        }

        response = self._request(
            f_name,
            'POST',
            url,
            auth=False,
            json_data=json_data
        )

        return self._process_response(f_name, response, f_args)

    def refresh_token(self) -> t.Dict:
        """
        Refresh token.
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = '/v1/usr/refresh_token/'

        json_data = {
            'refresh': self.__refresh_token,
        }

        response = self._request(
            f_name,
            'POST',
            url,
            auth=False,
            json_data=json_data,
        )

        return self._process_response(f_name, response, f_args)

    def user_info(self) -> t.Dict:
        """
        Get user info.

        :return: User info
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = '/v1/usr/info/'

        response = self._request(
            f_name,
            'GET',
            url,
            auth=True,
        )

        return self._process_response(f_name, response, f_args)

    def currencies_list(self, page: t.Optional[int] = 1) -> t.Dict:
        """
        Get currencies list.

        :param page: Page number (optional)
        :type page: int

        :return: Currencies list
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = '/v1/mkt/currencies/'

        params = {
            'page': page,
        }

        response = self._request(
            f_name,
            'GET',
            url,
            auth=False,
            params=params,
        )

        return self._process_response(f_name, response, f_args)

    def markets_list(self, page: t.Optional[int] = 1) -> t.Dict:
        """
        Get markets list.

        :param page: Page number (optional)
        :type page: int

        :return: Markets list
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = '/v1/mkt/markets/'

        params = {
            'page': page,
        }

        response = self._request(
            f_name,
            'GET',
            url,
            auth=False,
            params=params,
        )

        return self._process_response(f_name, response, f_args)

    def wallets(self) -> t.Dict:
        """
        Get wallets.

        :return: Wallets
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = '/v1/wlt/wallets/'

        response = self._request(
            f_name,
            'GET',
            url,
            auth=True,
        )

        return self._process_response(f_name, response, f_args)

    def orderbook(self, market_id: t.Union[int, MarketsIDs], side: t.Optional[str] = None) -> t.Dict:
        """
        Get orderbook.

        :param market_id: Market ID
        :type market_id: int

        :param side: Side (optional)
        :type side: str

        :return: Orderbook
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        if type(market_id) is MarketsIDs:
            market_id = market_id.value

        url = f'/v2/mth/actives/{market_id}/'

        side = side.lower() if side else None

        if side and side not in ['buy', 'sell']:
            raise BitpinExceptions(
                f_name,
                'Invalid side',
                f_args=f_args
            )
        else:
            params = {
                'type': side,
            }

        response = self._request(
            f_name,
            'GET',
            url,
            auth=False,
            params=params,
        )

        return self._process_response(f_name, response, f_args)

    def latest_trades(self, market_id: t.Union[int, CurrenciesIDs]) -> t.Dict:
        """
        Get latest trades.

        :param market_id: Market ID
        :type market_id: int

        :return: Latest trades
        :rtype: dict
        """

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        if type(market_id) is CurrenciesIDs:
            market_id = market_id.value

        url = f'/v1/mth/matches/{market_id}/'

        response = self._request(
            f_name,
            'GET',
            url,
            auth=False,
        )

        return self._process_response(f_name, response, f_args)

    def create_order(self, market: int, order_type: str, side: str, amount: float, price: float = None) -> t.Dict:

        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        if order_type.lower() == 'limit' and price is None:
            raise

        url = '/v1/odr/orders/'

        json_data = {
            'market': market,
            'mode': order_type,
            'type': side,
            'amount1': amount,
            'price': price,
            'price_limit': price,
        }

        response = self._request(
            f_name,
            'POST',
            url,
            auth=True,
            json_data=json_data
        )

        return self._process_response(f_name, response, f_args)

    def cancel_order(self, order_id: int) -> t.Dict:
        
        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = f'v1/odr/orders/{order_id}/'

        response = self._request(
            f_name,
            'DELETE',
            url,
            auth=True,
        )

        return self._process_response(f_name, response, f_args)
    
    def recent_trades(self):
        
        f_name = cf().f_code.co_name
        f_args = self.__get_func_args(locals())

        url = 'v1/odr/orders/'

        response = self._request(
            f_name,
            'GET',
            url,
            auth=True,
        )

        return self._process_response(f_name, response, f_args)