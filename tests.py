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

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    def test_add_new_book_empty_genre(self):
        self.collector.add_new_book('test')
        assert self.collector.books_genre.get('test') == ''

    def test_set_book_genre_set_genre(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert self.collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_set_incorrect_genre(self):
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мэшап')
        assert self.collector.books_genre.get('Что делать, если ваш кот хочет вас убить') == ''      

    def test_set_book_genre_set_incorrect_name(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Testbook', 'Ужасы')
        assert self.collector.books_genre.get('Гордость и предубеждение и зомби') == ''
    
    def test_get_book_genre_get(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.fixture(autouse=True)
    def predefined_collector(self):
        self.predefined_collector = BooksCollector()
        self.predefined_collector.add_new_book('Гиперион')
        self.predefined_collector.set_book_genre('Гиперион','Фантастика')

        self.predefined_collector.add_new_book('Дюна')
        self.predefined_collector.set_book_genre('Дюна','Фантастика')

        self.predefined_collector.add_new_book('Оно')
        self.predefined_collector.set_book_genre('Оно','Ужасы')

        self.predefined_collector.add_new_book('Кладбище домашних животных')
        self.predefined_collector.set_book_genre('Кладбище домашних животных','Ужасы')

        self.predefined_collector.add_new_book('Этюд в багровых тонах')
        self.predefined_collector.set_book_genre('Этюд в багровых тонах','Детективы')

        self.predefined_collector.add_new_book('Убийство в „Восточном экспрессе“')
        self.predefined_collector.set_book_genre('Убийство в „Восточном экспрессе“','Детективы')

        self.predefined_collector.add_new_book('Король Лев')
        self.predefined_collector.set_book_genre('Король Лев','Мультфильмы')

        self.predefined_collector.add_new_book('В поисках Немо')
        self.predefined_collector.set_book_genre('В поисках Немо','Мультфильмы')

        self.predefined_collector.add_new_book('Трое в лодке, не считая собаки')
        self.predefined_collector.set_book_genre('Трое в лодке, не считая собаки','Комедии')

        self.predefined_collector.add_new_book('Автостопом по галактике')
        self.predefined_collector.set_book_genre('Автостопом по галактике','Комедии')
        return self.predefined_collector
    
    def test_get_books_with_specific_genre_get_genre(self):
        mult = self.predefined_collector.get_books_with_specific_genre('Мультфильмы')
        assert 'Король Лев' in mult and 'В поисках Немо' in mult and len(mult) == 2

    def test_get_books_genre_get_books_genre(self):
        assert self.predefined_collector.get_books_genre() == self.predefined_collector.books_genre

    def test_get_books_for_children_get_books(self):
        children_books = self.predefined_collector.get_books_for_children()
        adulte_books = ['Оно', 'Кладбище домашних животных', 'Этюд в багровых тонах', 'Убийство в „Восточном экспрессе“']
        for i in adulte_books:
            assert i not in children_books

    def test_add_book_in_favorites_add_book(self):
        self.predefined_collector.add_book_in_favorites('Оно')
        assert 'Оно' in self.predefined_collector.favorites

    def test_delete_book_from_favorites(self):
        self.predefined_collector.add_book_in_favorites('Оно')
        self.predefined_collector.delete_book_from_favorites('Оно')
        assert len(self.predefined_collector.favorites) == 0

    def test_get_list_of_favorites_books_get_favorites(self):
        self.predefined_collector.add_book_in_favorites('Оно')
        self.predefined_collector.add_book_in_favorites('Дюна')
        fav = self.predefined_collector.get_list_of_favorites_books()
        assert 'Оно' in fav and 'Дюна' in fav and len(fav) == 2