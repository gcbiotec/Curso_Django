from django.urls import path
from .views import personList, person_new, persons_update, persons_delete

# Deve incluir /person/.. para acessar esta parte:
urlpatterns = [
    path('list/', personList, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>', persons_update, name='persons_update'),
    path('delete/<int:id>', persons_delete, name='persons_delete'),
]