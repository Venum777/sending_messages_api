from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from main.models import Messages
from main.serializers import(
    MessageSerializer, 
    MessageCreateSerializer
) 

class MessageViewSet(viewsets.ViewSet):
    """
    ViewSet for Game model.
    """

    queryset = Messages.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: MessageSerializer = MessageSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            message = self.queryset.get(pk=pk)
        except Messages.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = MessageSerializer(instance=message)
        return Response(data=serializer.data)
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message: Messages = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Message is created! Id: {message.pk}"
            }
        )
