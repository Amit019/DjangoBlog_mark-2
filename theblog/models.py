from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

# 1) category model

class Category(models.Model):
    name=models.CharField(max_length=50,default='unknown')

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('index')   
 
# !------------ end category model ------------------!
# !------------  Post model ------------------!

class Post(models.Model):
    title = models.CharField(max_length=250)
    author  =models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    category=models.CharField(max_length=50,default='unknown')
    snippets=models.CharField(max_length=250)
    thumbnail=models.ImageField(null=True , blank=True ,upload_to='static/upload/images/')
    publish = models.DateTimeField(auto_now_add=True)
    likes= models.ManyToManyField(User,related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('index')   

 
# !------------ end Post model ------------------!

# !------------ Profile model ------------------!

class Profile(models.Model):
    user=models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic=models.ImageField(null=True , blank=True ,upload_to='static/profile/images/')
    website_url = models.CharField(max_length=250,null=True , blank=True)
    facebook_url = models.CharField(max_length=250,null=True , blank=True)
    instagram_url = models.CharField(max_length=250,null=True , blank=True)
    twitter_url = models.CharField(max_length=250,null=True , blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')    

# !------------ end Profile model ------------------!

# !------------ Comment model ------------------!

class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")  
    name=models.CharField(max_length=250)   
    body=models.TextField()  
    date_added=models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return '%s -%s'% (self.post.title,self.name)

# !------------ end Comment model ------------------!


