from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'contact',views.ContactView,basename='contact')

urlpatterns = [
] + router.get_urls()