from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),  # Для получения списка и создания книги
    path('<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),  # Для работы с конкретной книгой
]
