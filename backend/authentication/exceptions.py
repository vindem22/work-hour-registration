from rest_framework import status
from rest_framework.exceptions import APIException


class CustomValidationError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def init(self, detail, status_code):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {'errors': (detail)}
        else:
            self.detail = {'errors': (self.default_detail)}
