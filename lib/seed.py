from faker import Faker
import random
from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import  Review, Book, Reader


engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def delete_records():
    session.query(Review).delete()
    session.query(Book).delete()
    session.query(Reader).delete()
    session.commit()

def create_records():
    reviews = [
        Review(
            rating = random.randint(1,6)
        ) for i in range(50)
    ]
    books = [
        Book(
            title = fake.unique.word(),
            author = fake.unique.name()
        ) for i in range (20)
    ]
    readers = [
        Reader(
            name = fake.unique.name(),
            age = random.randint(15, 50)
        ) for i in range (10)
    ]
    session.add_all(reviews + books + readers)
    session.commit()
    return reviews, books, readers

def relate_records(reviews, books, readers):
    for review in reviews:
        review.book = rc(books)
        review.reader = rc(readers)

    session.add_all(reviews + books + readers)
    session.commit()
    

if __name__ == '__main__':
    delete_records()
    reviews, books, passengers = create_records()
    relate_records(reviews, books, passengers)