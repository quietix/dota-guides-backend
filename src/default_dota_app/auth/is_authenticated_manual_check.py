from knox.auth import TokenAuthentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header


class IsAuthenticatedManualCheck(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if auth and auth[0].lower() == b'token':
            token = auth[1].decode('utf-8')
            try:
                user, auth_token = TokenAuthentication().authenticate_credentials(token.encode())
                return user, None
            except AuthenticationFailed:
                return None
        else:
            return None

    def authenticate_header(self, request):
        return 'Token'
