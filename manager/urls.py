# draw
# 신입생들이 동아리를 뽑기 위한 화면에 관련
from django.urls import path
from . import views
app_name = "manager"
urlpatterns = [
    path('', views.index, name="index"),
    path('draw_result', views.draw_result, name="draw_result"),
]
