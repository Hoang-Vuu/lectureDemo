class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return (f"I am {self.name}, {self.age} years old, {self.gender}")

class Member(Person):
    def __init__(self, name, age, gender, membershipid):
        self.membership = membershipid
        super().__init__(name, age, gender)

    def introduce(self):
        return (f"I am {self.name}, {self.age} years old, {self.gender}, with membership ID {self.membershipid}.")

class Author(Person):
    def __init__(self, name, age, gender, books_written):
        super().__init__(name, age, gender)
        self.books_written = books_written

    def list_books(self):
        return(f"Books written:{self.books_written}")


class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membershipid, books_written):
        Person.__init__(self, name, age, gender)
        self.books_written = books_written
        self.membershipid = membershipid
    def introduce(self):
        return (f"I am {self.name}, {self.age} years old, {self.gender}, with membership ID {self.membershipid}.")

Library_members=[
    AuthorMember("H", 23, "female","55757","hello"),
    AuthorMember("B", 45, "male", "668686","hi"),
    AuthorMember("K", 40, "female", "193939","chao")
]
for member in Library_members:
    print(member.introduce())