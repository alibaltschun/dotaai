from django.urls import path
from .views import home, drafting
from .utils.user_data import update_user_data, check_update

urlpatterns = [
    path('', home, name='home'),
    path('drafting', drafting, name='drafting'),
    path('drafting_check_update', check_update, name='check_update'),
    path('update_user_data/<str:arr_key>/<int:value>',
         update_user_data,
         name='update_user_data'),
]