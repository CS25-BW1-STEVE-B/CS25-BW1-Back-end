from .models import Player, Room, Item
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Player


class RoomSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Room


class ItemSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Item