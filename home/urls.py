from django.urls import path
from .views import home, my_logout

# Deve incluir /person/.. para acessar esta parte:
urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='my_logout'),
]