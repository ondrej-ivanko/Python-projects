from django.db import models

# Create your models here.

class Sport(models.Model):
    TYPE_CHOICES = (
            ("individual", "individual"), ("collective", "collective")
    )
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=False, blank=False,
                            help_text="collective or individual")
    sports = models.Manager()
    context = {
        "micovy": "Basketball",
        "atleticky": "Skok do dalky",
        "sporty": sports.all()
    }
    