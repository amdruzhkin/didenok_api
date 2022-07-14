from django.urls import path

from .views import *

urlpatterns = [
    path('imports', imports),
    path('delete/<id>', delete),
    path('nodes/<id>', nodes),
    path('sales/', sales),
    path('node/<id>/statistic', node_statistic),
]