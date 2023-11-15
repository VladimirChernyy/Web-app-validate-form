from django.urls import path
from .views import FormTemplateView

app_name = 'app'

urlpatterns = [
    path('get_form/', FormTemplateView.as_view(), name='get_form'),
]
