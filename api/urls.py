from django.urls import path
from . import views
from .views import PasswordChangeView

urlpatterns = [
    path('user' ,views.user_info , name = 'user-info'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),

]
