from .models import Link

def social_links(request):
    links = Link.objects.all()
    return {'links': links}