from rest_framework.routers import DefaultRouter

from .views import BasketViewSet, BasketGoodViewSet

router = DefaultRouter()
router.register('basket', BasketViewSet)
router.register('basketgood', BasketGoodViewSet)

urlpatterns = router.urls
