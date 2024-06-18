from django.contrib import admin
from django.urls import path,include
from app.views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'Company', Company)
router.register(r'Student', Student)
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token)
    

]