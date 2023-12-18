from django.urls import path
from . import views

urlpatterns = [
    path('static/',views.static_view,name="static"),
    path('database/list/',views.database,name="data") ,
    path('input/', views.user_text_input, name='user_text_input'),

]
