"""movieProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from boards.views import movieList, movieCreate, movieUpdate, movieDelete, movieListFilter, movieRecommended, movieSearch

urlpatterns = [
    url(r'^filter/(?P<category_id>\d+)/$', movieListFilter.as_view(), name='filter_category'),
    url(r'^recommended-movies/$', movieRecommended.as_view(), name='filter_recommended_movies'),
    url(r'^search/$', movieSearch.as_view(), name='search'),
    url(r'^$', movieList.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^movies/new', movieCreate.as_view(success_url="/"), name='new_movie'),
    url(r'^movies/edit/(?P<pk>\d+)/$', movieUpdate.as_view(success_url="/"), name='edit_movie'),
    url(r'^movies/delete/(?P<pk>\d+)', movieDelete.as_view(success_url="/"), name='delete_movie'),
]
