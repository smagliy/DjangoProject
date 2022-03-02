from django.db import models


class Cities(models.Model):
    city = models.TextField()
    country = models.TextField()

    def __str__(self):
        return f'{self.city}, {self.country}'
