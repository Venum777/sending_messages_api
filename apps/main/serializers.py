from rest_framework import serializers

from main.models import Messages
from auths.models import MyCustomUser


class MyUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()

    class Meta:
        model = MyCustomUser
        fields = [
            'username',
            'email',
            'phone_number'
        ]


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    message = serializers.TimeField()
    sender = MyUserSerializer()
    recipient = serializers.EmailField()
    how_many_messages = serializers.IntegerField()
    interval = serializers.IntegerField()

    class Meta:
        model = Messages
        fields = [
            'message',
            'sender',
            'recipient',
            'how_many_messages',
            'interval',
        ]

class MessageCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Messages
        fields = [
            'message',
            'sender',
            'recipient',
            'how_many_messages',
            'interval',
        ]