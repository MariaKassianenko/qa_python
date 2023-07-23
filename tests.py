import pytest
import random as r
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # метод добавления книги в словарь добавляет название в ключи словаря
    def test_add_new_book_true(self):
        collector = BooksCollector()
        name = 'Дюна'
        collector.add_new_book(name)
        assert name in collector.books_rating


    # всем новым добавляемым книгам присваивается рейтинг по умолчанию = 1
    @pytest.mark.parametrize('name', [
        'Дюна',
        'Властелин колец: Братство кольца',
        'Ешь, молись, люби'
    ])
    def test_add_new_book_rating_1(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_rating[name] == 1

    # метод добавление рейтинга книг от 1 до 10 добавляет верные значения в словарь
    @pytest.mark.parametrize('name, rating', [
        ['Дюна', 8],
        ['Властелин колец: Братство кольца', 10],
        ['Ешь, молись, люби', 3]
    ])
    def test_set_book_rating_from_1_to_10_true(self, name, rating):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.books_rating[name] == rating

    # добавление рейтинга за пределами диапазона значений или в виде строки - рейтинг остается на уровне по умолчанию 1
    @pytest.mark.parametrize('name, rating', [
        ['Дюна', 0],
        ['Властелин колец: Братство кольца', 11],
        ['Ешь, молись, люби', '0']
    ])
    def test_set_book_rating_not_from_1_to_10_rating_1(self, name, rating):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.books_rating[name] == 1

    # метод получения рейтинга по названию возвращает значение из словаря
    def test_get_book_rating_from_1_to_10_true(self):
        collector = BooksCollector()
        collector.books_rating = {
        'Дюна': 8,
        'Властелин колец: Братство кольца': 10,
        'Ешь, молись, люби': 3
        }
        for name in collector.books_rating:
            assert collector.get_book_rating(name) == collector.books_rating[name]

    # метод получения списка книг по указанному рейтингу (например, 10) возвращает список
    # книг, для каждой из которых рейтинг равен указанному значению (10)
    def test_get_books_with_specific_rating_10_true(self):
        collector = BooksCollector()
        collector.books_rating = {
        'Дюна': 8,
        'Властелин колец: Братство кольца': 10,
        'Ешь, молись, люби': 3
        }
        list_of_books_with_rating_10 = collector.get_books_with_specific_rating(10)
        for book in list_of_books_with_rating_10:
            assert collector.books_rating[book] == 10

    # метод выгрузки всего списка книг с рейтингами возвращает корректный словарь
    def test_get_books_rating_true(self):
        collector = BooksCollector()
        collector.books_rating = {
        'Дюна': 8,
        'Властелин колец: Братство кольца': 10,
        'Ешь, молись, люби': 3
        }
        assert collector.get_books_rating() == collector.books_rating

    # метод добавления книг в список любимых пополняет список предпочтений
    def test_add_book_in_favorites_two_books_true(self):
        collector = BooksCollector()
        collector.books_rating = {
            'Дюна': 8,
            'Властелин колец: Братство кольца': 10,
            'Ешь, молись, люби': 3
        }
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        assert len(collector.favorites) == 2

    # метод удаления книги из предпочтений приводит к уменьшению списка на соответствующее количество книг (пример, 1)
    def test_delete_book_from_favorites_one_book_len_favorites_less_one(self):
        collector = BooksCollector()
        collector.favorites = [
            'Дюна',
            'Властелин колец: Братство кольца'
        ]
        len_favorites = len(collector.favorites)
        name = r.choice(collector.favorites)
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == len_favorites - 1

    # метод запроса списка любимых книг возвращает корректный список предпочтений
    def test_get_list_of_favorites_book_true(self):
        collector = BooksCollector()
        collector.favorites = [
            'Дюна',
            'Властелин колец: Братство кольца'
        ]
        assert collector.get_list_of_favorites_books() == collector.favorites
