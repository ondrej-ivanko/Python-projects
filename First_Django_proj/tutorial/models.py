from django.db import models


class User(models.Model):
    #TextField je druh datatypu, který proměnná získá. viz manuál
    name = models.TextField()
    age = models.TextField()
