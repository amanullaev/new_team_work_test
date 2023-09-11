from django.urls import path
from yangilik.views import *

urlpatterns = [
    path('create_new/', CreateNewView.as_view()),
    path('get_all_news/', GetAllNewsView.as_view()),
    path('update_news/<int:id>/', UpdateNewView.as_view()),
    path('get_by_title/<str:title>/', DetailNewView.as_view()),
    path('delete_new/<int:id>/', DeleteNewView.as_view())
]