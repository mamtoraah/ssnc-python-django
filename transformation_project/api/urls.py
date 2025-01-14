from django.urls import path

from .views import SortNumbersView

urlpatterns = [
    path('sort-numbers/', SortNumbersView.as_view(), name='sort-numbers'),
]