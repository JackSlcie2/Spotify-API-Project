from .views import PacientesView
from django.urls import path, include

urlpatterns = [
    path('home', PacientesView.as_view())
]
