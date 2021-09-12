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
]



