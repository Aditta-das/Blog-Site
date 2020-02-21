from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User, auth
from account.models import User



class StyleOne(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORY = (
        ('Travel', 'Travel'),
        ('Lifestyle', 'Lifestyle'),
        ('Personal', 'Personal'),
        ('Brand', 'Brand'),
        ('Corporate', 'Corporate'),
        ('Finance', 'Finance'),
        ('Sports', 'Sports'),
        ('Business', 'Business'),
        ('Food', 'Food'),
        ('Cars', 'Cars'),
        ('Music', 'Music'),
        ('Games', 'Games'),
        ('Fitness', 'Fitness'),
        ('Entertainment', 'Entertainment'),
        ('Fashion', 'Fashion'),
        ('Politics', 'Politics'),
        ('Pets', 'Pets'),
    )
    category = models.CharField(max_length=15, choices=CATEGORY, default='Personal')
    blog = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("details", args=[self.id])



class Comment(models.Model):
    massage = models.TextField('massage')
    date_comment = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(StyleOne, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return '{} by {}'.format(self.user_id, self.post_id)

