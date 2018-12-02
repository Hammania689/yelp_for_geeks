from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    body = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='review_pics')
    # comments = models.ManyToOneRel(Comment)

    def __str__(self):
        return f"{self.title} by {self.author.username}"



# class Comment(models.Model):
#     author = models.OneToOneRel(User, on_delete=models.CASCADE)
#     body = models.TextField(max_length=3000)
#
#     def __str__(self):
#         return f"{self.author.username}"



