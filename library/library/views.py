from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        qs = super().get_queryset().order_by("-added_at")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(author__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["query"] = self.request.GET.get("q", "")
        return ctx


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("book-list")


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("book-list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")
