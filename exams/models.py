from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ikexam(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название экзамена")  # Поле 1
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")  # Поле 2
    exam_date = models.DateTimeField(verbose_name="Дата проведения экзамена")  # Поле 3
    image = models.ImageField(upload_to='exam_images/', verbose_name="Изображение задания", blank=True, null=True)  # Поле 4
    users = models.ManyToManyField(User, verbose_name="Пользователи")  # Поле 5
    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")  # Поле 6

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"