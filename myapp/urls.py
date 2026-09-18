from django.urls import include, path

from myapp import views
from django.contrib.sitemaps.views import sitemap
from myapp.sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('',views.home, name='home'),
    path('about/', views.about, name='aboutus'),
    path('leadership/', views.leadership, name='leadership'),
    path('events/', views.events, name='events'),
    path('contactus/', views.contactus, name='contactus'),
    path('ministries/', views.ministries, name='ministries'),
    path('gallery/', views.gallery, name='gallery'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path('test.xml', views.test_xml, name='test_xml'),
]