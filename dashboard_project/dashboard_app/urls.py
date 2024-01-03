from django.urls import path
from .views import AppListCreateView, AppDetailView, PlanListView, SubscriptionDetailView
# ,PlanDetailView, PlanListCreateView, 
from .views_auth import UserCreate, login

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', login, name='login'),
    path('apps/', AppListCreateView.as_view(), name='app-list-create'),
    path('apps/<int:pk>/', AppDetailView.as_view(), name='app-detail'),
    path('plans/', PlanListView.as_view(), name='plan-list'),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
    # URL patterns for Plan CRUD operations
    # path('plans/', PlanListCreateView.as_view(), name='plan-list-create'),
    # path('plans/<int:pk>/', PlanDetailView.as_view(), name='plan-detail'),
]