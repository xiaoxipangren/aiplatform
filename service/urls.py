from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from service import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'skill',views.SkillViewSet)
router.register(r'intent',views.IntentViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'auth/',include('rest_framework.urls',namespace='rest_framework'))
]
