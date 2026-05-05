from django.urls import path
from .views import ComplaintView, ComplaintIDView, ComplaintFilter, ComplaintDashboardView, ComplaintSearchView, ComplaintOrderingView, complaintPageView
from .views import *

urlpatterns =[
    path('complaintview/',ComplaintView.as_view()),
    path('complaintid/<int:id>/',ComplaintIDView.as_view()),
    path('filter/',ComplaintFilter.as_view()),
    path('dashboard/',ComplaintDashboardView.as_view()),
    path('search/',ComplaintSearchView.as_view()),
    path('order/',ComplaintOrderingView.as_view()),
    path('page/',complaintPageView.as_view()),
    path('login/',LogInAPI.as_view()),
    path('signup/',SignUpAPI.as_view())
]