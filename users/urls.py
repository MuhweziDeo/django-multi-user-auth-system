
from django.urls import path
from .views import OutLetCreateView,AdminstratorCreateView
from . import views

urlpatterns = [
    path('outlet/',OutLetCreateView.as_view()),
    path('admins/',AdminstratorCreateView.as_view()),
    path('login/',views.login_user)
]
