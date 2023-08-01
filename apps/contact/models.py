from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',
    message="Phone number must be entered in the format: '+998 __ ___ __ __'. Up to 13 digits allowed."
)


class GetInTouch(models.Model):
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17,
                                    blank=True, unique=True,
                                    help_text='for example: +998 __ ___ __ __')  # validators should be a list
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.message:
            return self.message
        return "None message"

