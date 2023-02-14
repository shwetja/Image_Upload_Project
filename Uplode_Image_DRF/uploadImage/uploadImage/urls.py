from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from uploadApp.views import ImageModelViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

router = SimpleRouter()
router.register('image', ImageModelViewSet, basename='image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('auth/', include('auth_app.urls')),
    path('token/', obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
