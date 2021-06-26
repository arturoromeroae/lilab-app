from clientapi.viewset import ClientViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientViewSet)
