from django.urls import path

from .views import IndexView, SignupView

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup')
]
