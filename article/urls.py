from django.urls import path
from .views import ArticleView

app_name = "arcticles"

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view())
]