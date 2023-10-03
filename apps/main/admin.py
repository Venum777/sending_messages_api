from django.contrib import admin
from .models import Messages


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = [
        'message', 
        'sender', 
        'recipient', 
        'how_many_messages', 
        'interval'
    ]
    list_filter = ['sender', 'recipient']