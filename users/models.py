from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    body = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='review_pics')
    # comments = models.ManyToOneRel(Comment)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})


# class Comment(models.Model):
#     author = models.OneToOneRel(User, on_delete=models.CASCADE)
#     body = models.TextField(max_length=3000)
#
#     def __str__(self):
#         return f"{self.author.username}"



