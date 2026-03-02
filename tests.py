import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['', 'aaaaabbbbbcccccdddddaaaaabbbbbcccccdddddaaaaa'])
    def test_add_new_book_incorrect_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_empty_genre(self, collector):
        collector.add_new_book('test')
        assert collector.books_genre.get('test') == ''

    def test_set_book_genre_set_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_set_incorrect_genre(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мэшап')
        assert collector.books_genre.get('Что делать, если ваш кот хочет вас убить') == ''      

    def test_set_book_genre_set_incorrect_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Testbook', 'Ужасы')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == ''
    
    def test_get_book_genre_get(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'
    
    def test_get_books_with_specific_genre_get_genre(self, predefined_collector):
        mult = predefined_collector.get_books_with_specific_genre('Мультфильмы')
        assert 'Король Лев' in mult and 'В поисках Немо' in mult and len(mult) == 2

    def test_get_books_genre_get_books_genre(self, predefined_collector):
        assert predefined_collector.get_books_genre() == predefined_collector.books_genre

    def test_get_books_for_children_get_books(self, predefined_collector):
        children_books = predefined_collector.get_books_for_children()
        adulte_books = ['Оно', 'Кладбище домашних животных', 'Этюд в багровых тонах', 'Убийство в „Восточном экспрессе“']
        for i in adulte_books:
            assert i not in children_books

    def test_add_book_in_favorites_add_book(self, predefined_collector):
        predefined_collector.add_book_in_favorites('Оно')
        assert 'Оно' in predefined_collector.favorites

    def test_delete_book_from_favorites(self, predefined_collector):
        predefined_collector.add_book_in_favorites('Оно')
        predefined_collector.delete_book_from_favorites('Оно')
        assert len(predefined_collector.favorites) == 0

    def test_get_list_of_favorites_books_get_favorites(self, predefined_collector):
        predefined_collector.add_book_in_favorites('Оно')
        predefined_collector.add_book_in_favorites('Дюна')
        fav = predefined_collector.get_list_of_favorites_books()
        assert 'Оно' in fav and 'Дюна' in fav and len(fav) == 2