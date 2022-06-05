from .views import HomePageView , SportPageView , SportDetailView , SportCreateView , SportUpdateView , SportDeleteView , CallMeView
from .views import TechnologyCreateView ,TechnologyPageView ,TechnologyDetailView , TechnologyUpdateView , TechnologyDeleteView
from .views import PoliticPageView , PoliticDetailView , PoliticCreateView , PoliticUpdateView , PoliticDeleteView
from django.urls import path
urlpatterns = [ 
    path('',HomePageView.as_view(),name='home'),
    path('sport/<int:pk>/delete/news/',SportDeleteView.as_view(),name='sport_news_delete'),
    path('sport/<int:pk>/edit/',SportUpdateView.as_view(),name='sport_news_edit'),
    path('sport/new_post/',SportCreateView.as_view(),name='sport_new_post'),
    path('sport_news/',SportPageView.as_view(),name='sport_news'),
    path('sport_detail/<int:pk>/',SportDetailView.as_view(),name='sport_detail'),
    path('technology/<int:pk>/delete/',TechnologyDeleteView.as_view(),name='technology_news_delete'),
    path('technology/<int:pk>/edit/' ,TechnologyUpdateView.as_view(),name='technology_news_edit'),
    path('technology/new_post/',TechnologyCreateView.as_view(),name='technology_new_post'),
    path('technology_news/',TechnologyPageView.as_view(),name='technology_news'),
    path('technology_detail/<int:pk>/',TechnologyDetailView.as_view(),name='technology_detail'),
    path('politic/<int:pk>/delete/news/',PoliticDeleteView.as_view(),name='politic_news_delete'),
    path('politic/<int:pk>/edit/',PoliticUpdateView.as_view(),name='politic_news_edit'),
    path('politic/new_post/',PoliticCreateView.as_view(),name='politic_new_post'),
    path('politic_news/',PoliticPageView.as_view(),name='politic_news'),
    path('politic_detail/<int:pk>/edit/',PoliticDetailView.as_view(),name='politic_detail'),
    path('callinformation/',CallMeView.as_view(),name='call_me'),
]