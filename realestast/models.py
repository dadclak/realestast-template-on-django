from django.db import models

# Create your models here.

class NewsBlock(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, null=True)
    image = models.ImageField(upload_to='news_block/', help_text='Service image')
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    pass