from django.db import models

# Create your models here.

class Sport(models.Model):
    TYPE_CHOICES = (
            ("individual", "individual"), ("collective", "collective")
    )
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=False, blank=False,
                            help_text="collective or individual")
    sports = models.Manager()

    def __str__(self):
        return self.type

class Mock(models.Model):
    url = models.CharField(max_length=150, null=True, blank=True)
    tiny = models.CharField(max_length=25, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
