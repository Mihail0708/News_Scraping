from bs4 import BeautifulSoup
import requests
from django.shortcuts import redirect
from django.views.generic import ListView

from News_Scraping.news.models import News


def create_news(request):
    News.objects.all().delete()
    url = "https://www.theonion.com/latest"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    info = soup.find_all('div', {"class": "sc-cw4lnv-13 hHSpAQ"})
    for article in info:
        main = article.find_all('a', href=True)
        linkx = article.find('a', {"class": "sc-1out364-0 dPMosf js_link"})
        link = linkx['href']
        imgx = main[0].find('img', src=True)
        image_src = imgx['data-src']
        titlex = article.find('h2', {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
        title = titlex.text
        new_content = News()
        new_content.title = title
        new_content.url = link
        new_content.image = image_src
        new_content.save()

    return redirect('news_home')


class NewsView(ListView):
    model = News
    template_name = 'home.html'
