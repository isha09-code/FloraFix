from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    # add extra fields if needed, e.g. phone, address, etc.

    def _str_(self):
        return self.full_name if self.full_name else self.user.username