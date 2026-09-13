from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from myapp.models import Event, Leader, Ministries, Gallery, Link
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    gallery_preview = Gallery.objects.order_by('-id')[:4]
    return render(request, 'home.html', {'gallery_preview': gallery_preview})

def about(request):
    return render(request, 'aboutus.html')

def leadership(request):
    senior = Leader.objects.filter(category="Senior Pastor")
    associate = Leader.objects.filter(category="Associate Pastor")
    ministry = Leader.objects.filter(category="Ministry Leader")
    return render(request, 'leadership.html', {'senior': senior, 'associate': associate, 'ministry': ministry})

def events(request):
    featured= Event.objects.filter(category="featured")
    upcoming= Event.objects.filter(category="upcoming")
    return render(request, 'events.html', {'featured': featured, 'upcoming': upcoming})

def contactus(request):

      if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
NEW CONTACT FORM SUBMISSION

------------------------------------------------------------

Name:
{name}

Email Address:
{email}

Subject:
{subject}

------------------------------------------------------------

Message:

{message}

------------------------------------------------------------

This message was sent from the Redeemed Gospel Church website.
"""

        email_message = EmailMessage(
            subject=f"Website Contact - {name}: {subject}",
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email],
        )

        email_message.send()

        messages.success(
            request,
            "✅ Thank you for contacting Redeemed Gospel Church. Your message has been sent successfully. We will get back to you as soon as possible."
        )
       
        return redirect("contactus")
    
      return render(request, "contactus.html")

def ministries(request):
    ministries = Ministries.objects.all()
    return render(request, 'ministries.html', {'ministries': ministries})

def gallery(request):
    worship = Gallery.objects.filter(category="Worship")
    conference = Gallery.objects.filter(category="Conference")
    youth = Gallery.objects.filter(category="Youth")
    outreach = Gallery.objects.filter(category="Outreach")
    other = Gallery.objects.filter(category="Other")
    return render(request, 'gallery.html',{'worship': worship, 'conference':conference, 'youth': youth, 'outreach' : outreach, 'other' : other})

def robots_txt(request):
 content = """User-agent: *
Allow: /
Sitemap: https://redeemed-gospel-church-sultan-hamud.onrender.com/sitemap.xml
    """
 return HttpResponse(content, content_type="text/plain")