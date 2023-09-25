from django.urls import reverse
from django.utils import timezone
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.author.pk})
    
    
    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    post = models.ForeignKey('blog.BlogPost',related_name='comments',on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_list", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title