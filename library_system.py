from enum import Enum, auto


class BookGenre(Enum):
    FICTION = auto()
    NON_FICTION = auto()
    SCIENCE = auto()
    HISTORY = auto()
    BIOGRAPHY = auto()


class MembershipLevel(Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500


class BookNotAvailableError(Exception):
    pass


class InvalidMembershipError(Exception):
    pass


class LateReturnError(Exception):
    pass


class Book:
    def __init__(self, title: str, genre: BookGenre, is_available: bool):
        self.title = title
        self.genre = genre
        self.is_available = is_available

    def borrow(self):
        if not self.is_available:
            raise BookNotAvailableError("Book is not available")
        self.is_available = False

    def return_book(self, is_late: bool):
        if is_late:
            raise LateReturnError("Book is returned late")
        self.is_available = True


class Member:
    def __init__(self, name: str, membership_level: MembershipLevel):
        self.name = name
        self.membership_level = membership_level

    def get_fee(self):
        if self.membership_level not in MembershipLevel:
            raise InvalidMembershipError("Invalid membership level")
        return self.membership_level.value
