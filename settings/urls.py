from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.main.views import MessageViewSet

router = DefaultRouter()
router.register(r'message', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls), name='message')
]
