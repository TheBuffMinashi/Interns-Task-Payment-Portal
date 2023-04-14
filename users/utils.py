import random

from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken


def code_generator():
    return str(random.randint(pow(10, 4), (pow(10, 5) - 1)))


def get_tokens_for_user(user):
    token = SlidingToken.for_user(user)

    return {
        'token': str(token),
        # 'access_token': str(refresh.access_token),
    }
