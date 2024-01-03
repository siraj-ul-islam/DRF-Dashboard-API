from rest_framework import generics, permissions
from .models import App, Plan, Subscription
from .serializers import AppSerializer, PlanSerializer, SubscriptionSerializer
from drf_yasg.utils import swagger_auto_schema

class PlanListView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny]  # Everyone can view the list of plans


# if you want to Use Plan CRUD operation as well
# class PlanListCreateView(generics.ListCreateAPIView):
#     queryset = Plan.objects.all()
#     serializer_class = PlanSerializer
#     permission_classes = [permissions.IsAdminUser]  # Only allow admin users to create or list all plans

# class PlanDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Plan.objects.all()
#     serializer_class = PlanSerializer
#     permission_classes = [permissions.IsAdminUser]  # Only allow admin users to update or delete plans

class AppListCreateView(generics.ListCreateAPIView):
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create and view their apps

    def get_queryset(self):
        # Restrict to only the apps owned by the current user
        return App.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Create an app instance and automatically subscribe it to the free plan
        app = serializer.save(owner=self.request.user)
        free_plan, created = Plan.objects.get_or_create(name=Plan.FREE, defaults={'price': 0.00})  # Ensure the free plan exists
        Subscription.objects.create(app=app, plan=free_plan)

class AppDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]  # Access is limited to the app's owner

    def get_queryset(self):
        # Restrict to only the apps owned by the current user
        return App.objects.filter(owner=self.request.user)

class SubscriptionDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only the subscription's app owner can update it

    def get_queryset(self):
        # Restrict to only the subscriptions associated with apps owned by the current user
        return Subscription.objects.filter(app__owner=self.request.user)

    def perform_update(self, serializer):
        # If a user wants to cancel their subscription, set it to inactive
        if 'active' in serializer.validated_data and not serializer.validated_data['active']:
            subscription = self.get_object()
            subscription.active = False
            subscription.save(update_fields=['active'])
        else:
            serializer.save()


