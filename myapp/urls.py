from django.urls import include, path

from myapp import views


urlpatterns = [
    path('',views.home, name='base'),
    path('about/', views.about, name='aboutus'),
    path('leadership/', views.leadership, name='leadership'),
    path('events/', views.events, name='events'),
    path('contactus/', views.contactus, name='contactus'),
    path('ministries/', views.ministries, name='ministries'),
    path('gallery/', views.gallery, name='gallery'),
]