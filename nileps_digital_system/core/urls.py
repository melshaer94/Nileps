from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet , home

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
#router.register(r'employees', EmployeeViewSet)
#router.register(r'tools', ToolViewSet)

urlpatterns = [
    path('', home),
    path('api/', include(router.urls)),

]
