from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model): #Модель хранения данных о постах
    title = models.CharField(max_length=150, db_index=True) #Поля данных title, slug, body, date
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title) #Возвращает формат в виде строки