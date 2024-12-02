from rest_framework import generics, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from rest_framework.pagination import PageNumberPagination
from typing import Any, Dict

# Класс для пагинации
class CustomPagination(PageNumberPagination):
    """
    Кастомный класс пагинации для отображения книг.
    - `page_size`: количество элементов на странице (по умолчанию 10).
    - `page_size_query_param`: параметр для задания размера страницы в запросе (по умолчанию 'page_size').
    - `max_page_size`: максимальное количество элементов на странице (по умолчанию 100).
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Класс для создания, отображения и поиска книг
class BookListCreateView(generics.ListCreateAPIView):
    """
    Класс для отображения списка книг и создания новых книг.

    Атрибуты:
    - `queryset`: все объекты Book, которые будут отображены.
    - `serializer_class`: сериализатор для объекта Book.
    - `pagination_class`: класс пагинации для ограничения количества книг на странице.
    - `filter_backends`: настройки для фильтрации и сортировки.
    - `filterset_class`: класс фильтрации книг.
    - `ordering_fields`: поля, по которым можно сортировать книги.
    - `ordering`: порядок сортировки по умолчанию.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination  # Используем свою пагинацию
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = BookFilter
    ordering_fields = ['title', 'author', 'year']
    ordering = ['title']

    def perform_create(self, serializer: Any) -> None:
        """
        Метод для создания новой книги.

        Добавляет книгу в базу данных с автоматическим присвоением статуса 'В наличии'.

        :param serializer: сериализатор для книги.
        """
        serializer.save(status='В наличии')

# Класс для получения, обновления и удаления книги
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс для получения, обновления и удаления книг.

    Атрибуты:
    - `queryset`: все объекты Book, которые могут быть получены, обновлены или удалены.
    - `serializer_class`: сериализатор для объекта Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request: Any, *args: tuple, **kwargs: Dict) -> Response:
        """
        Обновление книги в базе данных.

        :param request: объект запроса.
        :param args: дополнительные аргументы для метода.
        :param kwargs: дополнительные аргументы для метода.
        :return: объект Response с результатом обновления.
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request: Any, *args: tuple, **kwargs: Dict) -> Response:
        """
        Удаление книги из базы данных.

        :param request: объект запроса.
        :param args: дополнительные аргументы для метода.
        :param kwargs: дополнительные аргументы для метода.
        :return: объект Response с результатом удаления.
        """
        return super().destroy(request, *args, **kwargs)
