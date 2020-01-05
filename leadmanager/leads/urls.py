from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
# register([route], [viewset class], [name])

urlpatterns = router.urls