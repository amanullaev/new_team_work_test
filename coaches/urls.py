from django.urls import path
from .views import *

urlpatterns = [
    path('create_coach/', CreateCoachView.as_view()),
    path('get_all_coach/', GetAllCoachesView.as_view()),
    path('update_coach/<int:id>/', UpdateCoachView.as_view()),
    path('get_by_first_name/<str:first_name>/', DetailCoachView.as_view()),
    path('delete_coach/<int:id>/', DeleteCoachView.as_view())
]