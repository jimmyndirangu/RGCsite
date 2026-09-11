from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'aboutus', 'leadership', 'ministries', 'events','gallery','contactus']

    def location(self, item):
        return reverse(item)