from django.urls import path
from .views import (
    add_product,
    update_product,
    ProductListView,
    ProductDeleteView,
    hard_delete_product,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add/', add_product, name='add_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('hard-delete/<int:pk>/', hard_delete_product, name='hard_delete_product'),
]
