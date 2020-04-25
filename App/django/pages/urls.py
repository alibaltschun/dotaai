from django.urls import path
from .views import home, drafting

urlpatterns = [
    path('', home, name='home'),
    path('drafting', drafting, name='drafting'),
]