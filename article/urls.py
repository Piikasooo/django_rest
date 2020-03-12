from rest_framework.routers import DefaultRouter

from .views import ArticleVievSet

router = DefaultRouter()
router.register(r'articles', ArticleVievSet, basename='user')

urlpatterns = router.urls
