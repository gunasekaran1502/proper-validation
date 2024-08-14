from django.urls import path
from .views import submit_procurement, procurement_list, approval_list, approve_procurement

urlpatterns = [
    path('submit/', submit_procurement, name='submit_procurement'),
    path('list/', procurement_list, name='procurement_list'),
    path('approvals/', approval_list, name='approval_list'),
    path('approve/<int:pk>/', approve_procurement, name='approve_procurement'),
]