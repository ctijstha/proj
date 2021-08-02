from django.urls import path
from bmi.views import bmi_list, bmi_calculate, bmi_delete
app_name = 'bmi'


urlpatterns = [
    path('bmi-list/',bmi_list, name = 'bmi_list'),
    path('bmi-create/',bmi_calculate, name = 'bmi_calculate'),
    path('bmi-delete/<int:id>',bmi_delete, name = 'bmi_delete'),
    # path('product-add/',product_add, name = 'product_add'),
    # #path('product-add/',ProductAddView.as_view(), name = 'product_add'),
    # path('dashboard/',dashboard, name = 'dashboard'),
    # path('product-edit/<int:id>/',product_edit, name = 'product_edit'),
]