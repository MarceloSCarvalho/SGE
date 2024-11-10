from django.urls import path
from . import views


urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', views.BrandDetailsView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),

    path('api/v1/brand/', views.BrandCreateListApiView.as_view(), name='brand-create-list-api-view'),
    path('api/v1/brand/<int:pk>', views.BrandRetrieveUpadateDestroyAPIView.as_view(), name='brand-deteail-api-view')
]
