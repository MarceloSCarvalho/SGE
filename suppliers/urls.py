from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/detail/', views.SupplierDetailsView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/suppliers/', views.SupplierCreateListApiView.as_view(), name='supplier-create-list-api-view'),
    path('api/v1/suppliers/<int:pk>', views.SupplierRetrieveUpadateDestroyAPIView.as_view(), name='supplier-deteail-api-view')
]
