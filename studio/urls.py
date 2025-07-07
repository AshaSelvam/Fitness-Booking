from django.urls import path
from .auth_views import register, login_view
from .api import list_classes, book_class

urlpatterns = [
    path('classes/', list_classes, name='list_classes'),
    path('book/', book_class, name='book_class'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login')
]
