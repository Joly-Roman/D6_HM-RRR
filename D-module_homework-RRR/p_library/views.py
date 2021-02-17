
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author, Publisher, Friend
from django.shortcuts import redirect
from .forms import AuthorForm, BookForm, FriendForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render



def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)

    if request.method == 'POST':

        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():

            for author_form in author_formset:
                author_form.save()
                #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:

        author_formset = AuthorFormSet(prefix='authors')

    return render(request, 'manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
	    request,
		'manage_books_authors.html',
		{
	        'author_formset': author_formset,
			'book_formset': book_formset,
		}
	)


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'

class BookList(ListView):
    model = Book
    template_name = 'books_list.html'

class FriendList(ListView):
    model = Friend
    template_name = 'friends_list.html'


class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('friend_list')
    template_name = 'friend_edit.html'


class BookEdit(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    template_name = 'book_edit.html'




def publishers(request):
    template = loader.get_template('publishers_list.html')
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    publishers_data = {
        'publishers': publishers,
        'books': books
    }
    return HttpResponse(template.render(publishers_data, request))

def books(request):
    template = loader.get_template('books_list.html')
    books = Book.objects.all()
    books_data = {
        'books': books
    }
    return HttpResponse(template.render(books_data, request))

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')
