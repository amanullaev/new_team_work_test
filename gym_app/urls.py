from django.urls import path
from .views import *

urlpatterns = [
    path('create_gym/', CreateGymView.as_view()),
    path('get_all_gym/', GetAllGymView.as_view()),
    path('update_gym/<int:id>/', UpdateGymView.as_view()),
    path('get_by_name/<str:name>/', DetailGymView.as_view()),
    path('delete_gym/<int:id>/', DetailGymView.as_view())
]