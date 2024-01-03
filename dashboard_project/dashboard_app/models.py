from django.db import models
from django.conf import settings

class Plan(models.Model):
    FREE = 'free'
    STANDARD = 'standard'
    PRO = 'pro'
    PLAN_CHOICES = [
        (FREE, 'Free'),
        (STANDARD, 'Standard'),
        (PRO, 'Pro'),
    ]
    
    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class App(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    app = models.OneToOneField(App, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.app.name} - {self.plan.name}"