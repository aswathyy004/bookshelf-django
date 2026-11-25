from django.shortcuts import render, redirect
from .models import Book


def home(request):
    books = Book.objects.all()[:3]
    return render(request, 'app/home.html', {'featured': books})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'app/books.html', {'books': books})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'app/book_detail.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        year = request.POST['year']
        description = request.POST['description']

        book = Book(
            title=title,
            author=author,
            category=category,
            year=year,
            description=description
        )
        book.save()

        return redirect('book_list')

    return render(request, 'app/add_book.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.category = request.POST['category']
        book.year = request.POST['year']
        book.description = request.POST['description']

        book.save()

        return redirect('book_list')

    return render(request, 'app/edit_book.html', {'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'app/delete_book.html', {'book': book})


def about(request):
    return render(request, 'app/about.html')