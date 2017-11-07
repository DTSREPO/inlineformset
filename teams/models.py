from django.db import models


class Team(models.Model):
    name = models.CharField('Name', default='', max_length=32)

    def __str__(self):
        return self.name


POSITION_CHOICES = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five'),
)


class Member(models.Model):
    name = models.CharField('name', default='', max_length=32)
    team = models.ForeignKey(Team)
    position = models.CharField('Guard position', default='5', max_length=1, choices=POSITION_CHOICES)

    def __str__(self):
        return self.name
