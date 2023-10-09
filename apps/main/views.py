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
        search = request.query_params.get('srch', None)
        filter_message = request.query_params.get('filt', None)

        if search is not None:
            self.queryset = self.queryset.filter(
                recipient__contains=search
            )
        if filter_message is not None:
            if 'max' in filter_message:
                self.queryset = self.queryset.order_by('-how_many_messages')
            else:
                self.queryset = self.queryset.order_by('how_many_messages')

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
