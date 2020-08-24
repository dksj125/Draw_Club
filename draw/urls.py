# draw
# 신입생들이 동아리를 뽑기 위한 화면에 관련
from django.urls import path
from . import views
app_name = "draw"
urlpatterns = [
    path('', views.index, name="index"),
    path('choose_club', views.choose_club, name="choose_club"),
    path('select_finish', views.select_finish, name="select_finish"),
]
