from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='media', blank= True, null= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        user = super(Post, self).save(*args, **kwargs)
        # img = Image.open(self.image.path)
        # if img.height > 600 or img.width > 800:
        #     output_size = (600, 800)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
