from sqlalchemy import ForeignKey, Table, Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key= True)
    rating = Column(Integer())
    book_id = Column(ForeignKey('books.id'))
    reader_id = Column(ForeignKey('readers.id'))

    def __repr__(self):
        return f'Review Rating: {self.rating}'

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key = True)
    title = Column(String())
    author = Column(String())

    reviews = relationship('Review', backref = 'book')
    readers = association_proxy('reviews', 'reader', creator = lambda rd: Reviews(reader = rd))
    

    def __repr__(self):
        return f'{self.title} is written by {self.author}'

class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())

    reviews = relationship('Review', backref='reader')
    books = association_proxy('reviews', 'book', creator = lambda bk: Review(book=bk))

    def __repr__(self):
        return f'Reader: {self.name} Age: {self.age}'

