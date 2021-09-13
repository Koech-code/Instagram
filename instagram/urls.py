from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns=[
    url('^$', views.index, name='home'),
    url('logout/', LogoutView.as_view(), {"next_page": ''}),    
    url('profile/', views.profile, name='profile'),
    url('search/', views.search, name='search'),
    url('follow/(\d+)',views.following,name='follow'),
    url('like/(\d+)',views.like,name='like'),

]
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
