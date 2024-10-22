from django.urls import path
from .views import RegisterView, LoginView, PostViewSet
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, PostViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
] + router.urls

# Adicionei essa linha para arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
