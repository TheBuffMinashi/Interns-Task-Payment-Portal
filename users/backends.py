from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

user_model = get_user_model()


class PhoneOrEmailBackend(ModelBackend):
    """
    Custom authentication backend for allowing both email ond phone method of creating model
    """

    def authenticate(self, request, phone=None, email=None, password=None):
        try:
            user = user_model.objects.get(Q(phone=phone) | Q(email=email))
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            user_model().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
