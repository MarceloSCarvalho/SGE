from django.urls import path
from . import views


urlpatterns = [
    path('categories/list/', views.CategoriesListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoriesCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', views.CategoriesDetailsView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoriesUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoriesDeleteView.as_view(), name='category_delete'),

    path('api/v1/categories/', views.CategoryCreateListApiView.as_view(), name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>', views.CategoryRetrieveUpadateDestroyAPIView.as_view(), name='category-deteail-api-view')
]
