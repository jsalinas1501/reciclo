from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from trashcan.views import TrashCanViewSet, LevelViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'trash-cans', TrashCanViewSet)
router.register(r'levels', LevelViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Home.
    url(r'^', include('home.urls', namespace='home_app')),
    # Trashcan.
    url(r'^cans/', include('trashcan.urls', namespace='trashcan_app')),
    # DRF.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
