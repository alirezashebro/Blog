from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='نویسنده', on_delete=models.CASCADE)
    title = models.CharField('عنوان', max_length=200)
    text = models.TextField('شرح')
    created_date = models.DateTimeField('تاریخ ایجاد', default=timezone.now)
    published_date = models.DateTimeField('تاریخ انتشار', blank=True, null=True)
    modified_date = models.DateTimeField('آخرین زمان ویرایش', blank=True, null=True)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    