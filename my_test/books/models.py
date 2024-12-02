from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('В наличии', 'В наличии'),
        ('Выдана', 'Выдана'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.CharField(max_length=255, verbose_name="Автор книги")
    year = models.IntegerField(verbose_name="Год издания")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available', verbose_name="Статус")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
