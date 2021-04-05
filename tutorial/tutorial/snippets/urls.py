from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'snippets', views.UserViewSEt)


urlpatterns = [
    path('', include(router.urls))
]