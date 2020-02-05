from django.db import models

# Create your models here.
class Player(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)
    inventory = models.ForeignKey(Item, on_delete=models.CASCADE)


    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print('path is blocked')


class Room(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    player = models.ForeignKey(Player)

    def get_room_in_direction(self, direction):
        if direction == 'n':
            return self.n_to 
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to 
        elif direction == 'w':
            return self.w_to 
            


class Item(models.model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=128)

