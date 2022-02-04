from django.urls import path
from main.views import (
    HomepageView
)

urlpatterns = [
    path('', HomepageView.as_view(), name='home-page')
]