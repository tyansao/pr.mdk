from django.contrib.sessions.backends.base import SessionBase
from someapp.models import Book

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'

    def __init__(self, session: dict) -> None:
        self.session : dict = session
        self.cart = self.session.get(self.CART_SESSION_ID)

        if not self.cart:
            self.cart = self.session[self.CART_SESSION_ID] = {}

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        cart = self.cart.copy()

        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session.modified = True

    def add(self, book, quantity=1, update_quantity=False):
        book_id = str(book.id)

        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0, 'price': book.price}

        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity

        self.save()

    def remove(self, book):
        book_id = str(book.id)

        if book_id in self.cart:
            if self.cart[book_id]['quantity'] > 1:
                self.cart[book_id]['quantity'] -= 1
            else:
                del self.cart[book_id]
            self.save()

    def remove_all(self, book):
        book_id = str(book.id)

        if book_id in self.cart:
            if self.cart[book_id]['quantity'] > 1:
                self.cart[book_id]['quantity'] = 0
            else:
                del self.cart[book_id]
            self.save()

    def get_total_price(self):
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()

    