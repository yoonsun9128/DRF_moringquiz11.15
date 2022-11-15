from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name="users"


urlpatterns = [
    # user/
    path('', views.UserView.as_view(), name="signup"),
    path('api/token/', views.SpartaTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]