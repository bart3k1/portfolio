from django.db import models
from django.utils import timezone


class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def summary(self):
        return self.body[:100] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")

    def __str__(self):
        return 'Blog: {}'.format(self.title)
