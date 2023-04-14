import uuid

from django.core.cache import cache
from celery import shared_task
from celery.utils.log import get_task_logger

from users.utils import code_generator


logger = get_task_logger(__name__)


@shared_task
def send_verification_code(phone=None, email=None):
    if phone and email:
        phone_verification_code = code_generator()
        email_verification_code = code_generator()
        cache.set(phone, phone_verification_code, 120)
        cache.set(email, email_verification_code, 120)
        # Email and phone sending APIs
        logger.info(f'Verification code: {phone_verification_code}')
        logger.info(f'Verification code: {email_verification_code}')
    elif phone:
        phone_verification_code = code_generator()
        cache.set(phone, phone_verification_code, 120)
        logger.info(f'Verification code: {phone_verification_code}')
    elif email:
        email_verification_code = uuid.uuid4().hex
        cache.set(email, email_verification_code, 120)
        logger.info(f'Verification code: {email_verification_code}')
    else:
        logger.info("Invalid Input")
