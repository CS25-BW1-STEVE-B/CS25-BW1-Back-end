from django.db import models

# Create your models here.
class Player(models.model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)
    inventory = models.ForeignKey(Item, on_delete=models.CASCADE)


class Room(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    player = models.ForeignKey(Player)


class Item(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)

