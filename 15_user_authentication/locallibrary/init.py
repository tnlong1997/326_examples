import textwrap
from datetime import timedelta, date


from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker

from catalog.models import Author, Book, BookInstance, Genre

fake = Faker()

# Create Genres
genres = [
    Genre(name="Science Fiction"),
    Genre(name="Satire"),
    Genre(name="Drama"),
    Genre(name="Adventure"),
    Genre(name="Romance"),
    Genre(name="Mystery"),
]

# Save the genres to the database
for genre in genres:
    genre.save()

# Create Authors
authors = []
for i in range(1, 10):
    a_fname = fake.first_name()
    a_lname = fake.last_name()
    a_dob = fake.date_of_birth()
    a_dod = a_dob + timedelta(days=365 * fake.random_int(65, 100))
    author = Author(
        first_name=a_fname, last_name=a_lname, date_of_birth=a_dob, date_of_death=a_dod
    )
    author.save()
    authors.append(author)


# Create Books
books = []
for i in range(1, 10):
    a_title = fake.text(50)
    a_author = authors[fake.random_int(0, len(authors)) - 1]
    a_summary = fake.text(1000)
    a_isbn = fake.isbn13()
    book = Book(title=a_title, author=a_author, summary=a_summary, isbn=a_isbn)
    book.save()
    book.genre.add(genres[fake.random_int(0, len(genres)) - 1])
    book.save()
    books.append(book)

instances = []
for i in range(1, 400):
    a_book = books[fake.random_int(0, len(books)) - 1]
    a_imprint = fake.text(200)
    a_status = "a"
    instance = BookInstance(book=a_book, imprint=a_imprint, status=a_status)
    instance.save()
    instances.append(instance)

print("Genre:")
for g in Genre.objects.all():
    print(g)

print("\nAuthor:")
for a in Author.objects.all():
    print(a)

print("\nBook:")
for b in Book.objects.all():
    print(b)

print("\nBookInstance:")
for i in BookInstance.objects.all():
    print(i)

# Retrieve a random book from model and print it.
books_count = Book.objects.count()
book = Book.objects.all()[fake.random_int(0, books_count - 1)]

print("\nExample Book:")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"ISBN: {book.isbn}")
print(f"Summary:\n{textwrap.fill(book.summary, 77)}")


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080
====================================================================
"""
print(message)

# NEW 17
ct = ContentType.objects.get_for_model(BookInstance)
permission = Permission.objects.get(
    codename="can_mark_returned", name="Set book as returned", content_type=ct
)

# Create and add users
users = []
print("Generated users:")
for a in authors:
    username = a.first_name.lower()[0] + a.last_name.lower()
    email = f"{username}@326.edu"
    password = a.last_name
    user = User.objects.create_user(username, email, password)
    user.first_name = a.first_name
    user.last_name = a.last_name
    user.user_permissions.add(permission)
    user.save()
    users.append(user)
    print(f"  username: {username}, password: {password}")

print("\nUsers who have a book on loan:")
for i in range(0, 20):
    book_instance = instances[fake.random_int(0, len(instances)) - 1]
    a_user = users[fake.random_int(0, len(users)) - 1]
    book_instance.borrower = a_user
    book_instance.status = "o"
    a_delta = timedelta(days=fake.random_int(1, 4))
    book_instance.due_back = date.today() + a_delta
    book_instance.save()
    print(f"  {a_user.username}")
