from django.conf.urls import include, url
from . import views

urlpatterns = [
    #/user/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/Movie/movie_id/
    url(r'^(?P<pk>[0-9]+)/$',views.Index1View.as_view(),name='detail'),
    url(r'user/add/$', views.MovieCreate.as_view(),name='movie-add'),
    url(r'user/(?P<pk>[0-9]+)/$',views.MovieUpdate.as_view(),name='movie-up'),
    url(r'user/(?P<pk>[0-9]+)/delete$',views.MovieDelete.as_view(),name='movie-del'),

    url(r'^register/$',views.UserFormView.as_view(),name='register'),

]