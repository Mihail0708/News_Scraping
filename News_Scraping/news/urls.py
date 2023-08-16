from django.urls import path

from News_Scraping.news import views
from News_Scraping.news.views import NewsView

urlpatterns = [
    path('generate/', views.create_news, name='news_create'),
    path('', NewsView.as_view(), name='news_home')
]