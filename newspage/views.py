from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView
from django.views.generic.edit import CreateView ,UpdateView
from .models import AuthorSportPage , AuthorTechnologyPage , AuthorPoliticPage
# Create your views here.
class HomePageView(ListView):
    model=AuthorSportPage
    template_name="home.html"
    
class SportPageView(ListView):
    model=AuthorSportPage
    template_name='sport_news.html'
    
class SportDetailView(DetailView):
    model=AuthorSportPage
    context_object_name='sport'
    template_name='sport_detail.html'
    
class SportCreateView(CreateView):
    model=AuthorSportPage
    template_name='sport_new_post.html'
    fields=['title','author','text']
    
class SportUpdateView(UpdateView):
    model=AuthorSportPage
    context_object_name='sport'
    template_name='sport_news_edit.html'
    fields=['title','text']
   
class TechnologyPageView(ListView):
    model=AuthorTechnologyPage
    template_name='technology_news.html'
    
class TechnologyDetailView(DetailView):
    model=AuthorTechnologyPage
    context_object_name='technology'
    template_name='technology_detail.html'
    
class TechnologyCreateView(CreateView):
    model=AuthorTechnologyPage
    template_name='technology_new_post.html'
    fields= ['title','author','text']
    
class TechnologyUpdateView(UpdateView):
    model=AuthorTechnologyPage
    context_object_name='technology'
    template_name='technology_news_edit.html'
    fields= ['title','text']
       
class PoliticPageView(ListView):
    model=AuthorPoliticPage
    template_name= 'politic_news.html'
    
class PoliticDetailView(DetailView):
    model=AuthorPoliticPage
    context_object_name='politic'
    template_name='politic_detail.html' 
    
class PoliticCreateView(CreateView):
    model=AuthorPoliticPage
    template_name='politic_new_post.html'
    fields=['title','author','text']
    
class PoliticUpdateView(UpdateView):
    model=AuthorPoliticPage
    context_object_name='politic'
    template_name='politic_news_edit.html'
    fields=['title','text']
    
class CallMeView(TemplateView):
    template_name='call_me.html'