from django.urls import path
from .views import notice, single_notice


urlpatterns = [
    path('', notice, name='notices'),
    path('<str:heading>/', single_notice, name='notice')
]
