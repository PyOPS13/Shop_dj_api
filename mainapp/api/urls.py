from django.urls import path
from .api_views import CategoryApiView, NotebookListApiView, NotebookDetailApiView, CustomersListApiView

urlpatterns = [
    path('categories/<str:id>/', CategoryApiView.as_view(), name='categories_list'),
    path('customers/', CustomersListApiView.as_view(), name='customer_list'),
    path('notebooks/', NotebookListApiView.as_view(), name='notebooks_list'),
    path('notebooks/<str:id>/', NotebookDetailApiView.as_view(), name='notebook_detail')
]