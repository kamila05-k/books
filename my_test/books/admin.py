from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'status')  # Поля для отображения в списке
    list_filter = ('status', 'year')  # Фильтры для списка
    search_fields = ('title', 'author')  # Поля для поиска
    ordering = ('title',)  # Сортировка по названию книги

# Регистрация модели и её администратора
admin.site.register(Book, BookAdmin)