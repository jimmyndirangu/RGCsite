from django.db import models

# Create your models here.
class Leader(models.Model):
    CATEGORY=[
        ("Senior Pastor", "Senior Pastor"),
        ("Associate Pastor", "Associate Pastor"),
        ("Ministry Leader", "Ministry Leader"),
    ]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    image = models.ImageField(upload_to="leaders/")
    message = models.TextField()

    def __str__(self):
        return self.name

class Ministries(models.Model):
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    meeting_time = models.CharField(max_length=100)
    meeting_day = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="ministries/")

    def __str__(self):
        return self.name

class Event(models.Model):
    CATEGORY=[
        ("featured", "featured"),
        ("upcoming", "upcoming"),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    image = models.ImageField(upload_to="events/")
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    CATEGORY=[
        ("Worship", "Worship"),
        ("Conference", "Conference"),
        ("Youth", "Youth"),
        ("Outreach", "Outreach"),
        ("Other", "Other"),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/")
    category = models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self):
        return self.title

class Link(models.Model):
    platform = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.platform
