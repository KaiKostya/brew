import requests
from utils.logger.logger import Logger


class BaseRequest:
    """request functionality"""

    _base_url = "https://api.openbrewerydb.org/breweries"
    cert_path = "cert.pem"
    _headers = {"Content-Type": "application/json; charset=utf-8", "x-date-format": "ISO"}

    @staticmethod
    def get(command: str, params="") -> requests.Response:
        """command is a name of resource, params if not empty - query params after ? sign"""
        try:
            if params != "":
                str_param = f"?{params}"
            else:
                str_param = params
            endpoint = f"{BaseRequest._base_url}/{command}" + str_param
            response = None
            response = requests.get(endpoint, cert=BaseRequest._cert, headers=BaseRequest._headers)
            return response
        except Exception:
            Logger.tests_logger.exception("Exception")
            return response
