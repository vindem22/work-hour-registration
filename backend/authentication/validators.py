from django.contrib.auth import authenticate
from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuthValidator(OAuth2Validator):
    def validate_user(
        self, username, password, client, request, *args, **kwargs
    ):
        """
        Check username and password correspond to a valid
        """
        u = authenticate(username=username, password=password)
        print(u)
        if u is not None:
            print(u.user)
            if u.user is not None:
                request.user = u
                print(request.user)
                return True
        return False
