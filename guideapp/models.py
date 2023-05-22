from django.db import models
from django.utils.translation import gettext_lazy as _


class MultilingualText(models.Model):
    key = models.CharField(max_length=255)
    languages = models.CharField(max_length=2, choices=[
        ('en', _('English')),
        ('es', _('Spanish')),
        ('uk', _('Ukrainian'))
    ], default='es')
    content = models.TextField()

    class Meta:
        unique_together = ('key', 'languages')  # updated this line

    def __str__(self):
        return f'{self.key} - {self.languages} - {self.content}'


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.created_at}'
