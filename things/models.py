from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def create_user(self, name, description, quuantity):
        if not name:
            raise ValueError("An name must be provided.")

        user = self.model(name=name, **extra_fields)
        user.save()

        return user
