from django.db import models


class FeedBack(models.Model):
    name = models.CharField('Название модели', max_length = 120)
    email = models.EmailField('Email', max_length = 120, blank = True, null = True)
    phone = models.CharField('Телефон номера',max_length = 15 )
    description = models.CharField('Описание',max_length = 120, blank = True, null = True)
    call_time = models.CharField('Время звонка', max_length = 120, blank = True, null = True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'