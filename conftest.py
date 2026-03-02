import pytest
from main import BooksCollector

@pytest.fixture(autouse=True)
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(autouse=True)
def predefined_collector():
    predefined_collector = BooksCollector()
    predefined_collector.add_new_book('Гиперион')
    predefined_collector.set_book_genre('Гиперион','Фантастика')

    predefined_collector.add_new_book('Дюна')
    predefined_collector.set_book_genre('Дюна','Фантастика')

    predefined_collector.add_new_book('Оно')
    predefined_collector.set_book_genre('Оно','Ужасы')

    predefined_collector.add_new_book('Кладбище домашних животных')
    predefined_collector.set_book_genre('Кладбище домашних животных','Ужасы')

    predefined_collector.add_new_book('Этюд в багровых тонах')
    predefined_collector.set_book_genre('Этюд в багровых тонах','Детективы')

    predefined_collector.add_new_book('Убийство в „Восточном экспрессе“')
    predefined_collector.set_book_genre('Убийство в „Восточном экспрессе“','Детективы')

    predefined_collector.add_new_book('Король Лев')
    predefined_collector.set_book_genre('Король Лев','Мультфильмы')

    predefined_collector.add_new_book('В поисках Немо')
    predefined_collector.set_book_genre('В поисках Немо','Мультфильмы')

    predefined_collector.add_new_book('Трое в лодке, не считая собаки')
    predefined_collector.set_book_genre('Трое в лодке, не считая собаки','Комедии')

    predefined_collector.add_new_book('Автостопом по галактике')
    predefined_collector.set_book_genre('Автостопом по галактике','Комедии')
    return predefined_collector