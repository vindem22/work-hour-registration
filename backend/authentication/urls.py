from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from authentication.views import AuthViewSet, UserToken
from django.urls import include, path


router = routers.DefaultRouter()
router.register('v1/auth', AuthViewSet)

urlpatterns = []

app_name = 'authentication'
urlpatterns += router.urls
urlpatterns += [
    path('v1/auth/token/', UserToken.as_view(), name='token'),
    path('v1/auth/', include('rest_framework_social_oauth2.urls')),
]