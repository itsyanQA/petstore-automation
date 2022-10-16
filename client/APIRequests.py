import json
from typing import Union, Final
import requests
import logging as logger


class APIRequests:
    BASE_URL: Final[str] = "https://petstore.swagger.io/v2"

    @staticmethod
    def http_get(url: str, params=None, should_ignore_exception: bool = False):
        """Generic GET request method"""
        try:
            logger.info(f"Sending GET Request To: [{url}]")
            request = requests.request("GET", url, params=params)
            response: requests.models.Response = request
            if not should_ignore_exception:
                response.raise_for_status()
            return response
        except Exception as e:
            logger.error(f"GET Request has failed with the exception of: [{e}]")
            return None

    @staticmethod
    def http_post(url: str, body: Union[dict, str] = None, is_form_data: bool = False):
        """Generic POST request method"""
        logger.info(f"Sending POST Request To: [{url}], with body [{body}]")
        if is_form_data:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            request = requests.post(url=url, data=body, headers=headers)
            response: requests.models.Response = request
            return response
        else:
            request = requests.post(url=url, json=json.loads(body))
            response: requests.models.Response = request
            return response

    @staticmethod
    def http_delete(url: str):
        """Generic DELETE request method"""
        logger.info(f"Sending DELETE Request To: [{url}]")
        request = requests.delete(url=url)
        response: requests.models.Response = request
        return response

    @staticmethod
    def http_put(url: str, body: str):
        """Generic PUT request method"""
        logger.info(f"Sending PUT Request To: [{url}]")
        request = requests.put(url=url, json=json.loads(body))
        response: requests.models.Response = request
        return response

