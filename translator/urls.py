from . import views
from django.urls import path


urlpatterns = [
    path('', views.translator_view, name='translate_view')
]
