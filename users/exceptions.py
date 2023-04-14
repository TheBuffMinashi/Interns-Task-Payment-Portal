from rest_framework.exceptions import APIException


class PhoneOrEmailNotEntered(APIException):
    status_code = 400
    default_detail = 'An email or a phone number must be entered.'
    default_code = 'invalid_data'


class VerificationCodeExpiredOrInvalid(APIException):
    status_code = 400
    default_detail = 'The verification code entered has expired or the phone number is invalid.'
    default_code = 'invalid_verification_code'


class VerificationCodeInvalid(APIException):
    status_code = 400
    default_detail = 'The verification code entered is invalid.'
    default_code = 'invalid_verification_code'


class InvalidPhoneOrEmail(APIException):
    status_code = 400
    default_detail = 'The email address or the phone number you entered is invalid.'
    default_code = 'invalid_email_or_phone'


class WrongPassword(APIException):
    status_code = 400
    default_detail = 'The password entered is wrong.'
    default_code = 'wrong_password'


class UserNotVerified(APIException):
    status_code = 400
    default_detail = 'User email address or phone number is not verified.'
    default_code = 'user_not_verified'


class InvalidPhoneEntry(APIException):
    status_code = 400
    default_detail = 'The phone number you entered is invalid.'
    default_code = 'invalid_phone'


class PhoneAlreadyVerified(APIException):
    status_code = 400
    default_detail = 'The phone number you entered is already verified.'
    default_code = 'phone_already_verified'


class InvalidEmailEntry(APIException):
    status_code = 400
    default_detail = 'The phone number you entered is invalid.'
    default_code = 'invalid_email'


class EmailAlreadyVerified(APIException):
    status_code = 400
    default_detail = 'The email address you entered is already verified.'
    default_code = 'email_already_verified'
