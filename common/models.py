from django.db import models


class BaseModel(models.Model):
    """

    Provides a simple and convenient way to add created_at, updated_at and is_active fields
    to any model that inherits from it, helps to build
    more robust and maintainable applications with less code.

    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True
