from django.db import
from django.contrib.auth.models import User

class skills(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_science = models.PositiveIntegerField()
    business = models.PositiveIntegerField()
    computer_science = models.PositiveIntegerField()
    math_logic = models.PositiveIntegerField()
    physical_science = models.PositiveIntegerField()
    art_humanities = models.PositiveIntegerField()
    social_sciences = models.PositiveIntegerField()
    life_science = models.PositiveIntegerField()
    language = models.PositiveIntegerField()

    def __str__(self):
        return self.user