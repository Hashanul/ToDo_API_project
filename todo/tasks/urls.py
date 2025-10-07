from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, 
    TokenVerifyView,
)

urlpatterns = [
    path('task/', views.TaskCreateView.as_view()),
    path('task/<int:pk>/', views.TaskDetailView.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
# jwt    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

# using Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

