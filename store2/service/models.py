from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Название категории', max_length = 120)
    slug = models.SlugField('URL', max_length = 120)
    text = models.TextField('Текст категории')
    banner = models.ImageField('Баннер', upload_to = 'images/', blank = True, null = True)
    title = models.CharField('Title', max_length = 120)
    description = models.CharField('Description', max_length = 120)
    keywords = models.CharField('Keywords', max_length = 120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Model(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True,verbose_name = 'Выбор категории')
    name = models.CharField('Название услуги', max_length = 120)
    slug = models.SlugField('URL', max_length = 120, default = '', unique = True)
    text = models.TextField('Текст модели',default = '')
    price = models.CharField('Цена', max_length=120, blank=True, null=True)
    header = models.CharField('Заголовок', max_length = 120, blank = True, null = True)
    sub_header = models.CharField('Подзаголовок', max_length = 120, blank = True, null = True)
    images = models.ImageField('Картинка', upload_to = 'images/', blank = True, null = True)
    active = models.BooleanField('Опубликовать',default = True)
    title = models.CharField('Title', max_length = 200)
    description = models.TextField('Description')
    kyewords = models.CharField('Keywords', max_length = 250)
    sort = models.CharField('Порядок', default=0, unique=True, max_length = 250)
    banner = models.ImageField('Banner', upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_model_view', kwargs={'category': self.category.slug, 'slug':self.slug})

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    
