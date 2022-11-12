from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Почта")
    text = models.TextField(max_length=500, null=False, blank=False, verbose_name="Текст Записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name='Статус')

    def __str__(self):
        return f"Запись {self.pk}: {self.author}"
