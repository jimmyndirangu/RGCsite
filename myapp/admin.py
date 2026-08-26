from django.contrib import admin
from myapp.models import Event, Leader, Link, Ministries, Gallery

# Register your models here.
admin.site.register(Leader)
admin.site.register(Ministries)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Link)