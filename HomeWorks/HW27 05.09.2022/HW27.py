class Auto:
    def __init__(self, model_name: str, year: int, producer: str, engine_volume: float, color: str, price: float):
        self.model = model_name
        self.year = year
        self.producer = producer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def get_all_items(self):
        return f"Model: {self.model}    Year: {self.year}   Producer: {self.producer}\n" \
               f"Engine Volume: {self.engine_volume}    Color: {self.color}     Price: {self.price}"

    def get_model_name(self):
        return self.model

    def get_year(self):
        return self.year

    def get_producer(self):
        return self.producer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


class Book:
    def __init__(self, name: str, year: int, publisher: str, genre: str, author: str, price: float):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_all_items(self):
        return f"Name: {self.name}    Year: {self.year}   Publisher: {self.publisher}\n" \
               f"Genre: {self.genre}    Author: {self.author}     Price: {self.price}"

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    @staticmethod
    def is_big(page_num: int):
        if page_num >= 100:
            return True
        else:
            return False


class Stadium:
    def __init__(self, name: str, opening_year: int, country: str, city: str, capacity: int):
        self.name = name
        self.opening_year = opening_year
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_all_items(self):
        return f"Name: {self.name}    Opening year: {self.opening_year}   Country: {self.country}\n" \
               f"City: {self.city}    Capacity: {self.capacity}"

    def get_name(self):
        return self.name

    def get_opening_year(self):
        return self.opening_year

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity


class SchoolBook(Book):
    def __init__(self, name: str, year: int, publisher: str, genre: str, author: str, price: float, class_num: int):
        super().__init__(name, year, publisher, genre, author, price)
        self.class_num = class_num

    def is_the_schoolbook_correct(self):
        tmp = 2022 - (5 + self.class_num)
        if tmp >= 30:
            print("Book is old")
        else:
            print("Book is normal")

    def get_all_items(self):
        return f"Name: {self.name}    Year: {self.year}   Publisher: {self.publisher}\n" \
               f"Genre: {self.genre}    Author: {self.author}     Price: {self.price}   Class Number: {self.class_num}"


auto1 = Auto('Toyota', 2010, 'Japan', 2.4, 'gray', 5500)
# print(auto1.get_all_items())
# print(auto1.get_price())

school_book = SchoolBook("History", 2005, "Almaty Kitap", 'school_books', "Almaty Kitap", 20, 10)
print(school_book.get_all_items())
print(school_book.is_big(200))
