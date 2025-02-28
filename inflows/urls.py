from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailsView.as_view(), name='inflow_detail'),

    path('api/v1/inflows/', views.InflowCreateListApiView.as_view(), name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>', views.InflowRetrieveAPIView.as_view(), name='inflow-deteail-api-view')
]
