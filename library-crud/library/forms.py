from django import forms
from .models import Book

INPUT_CLASS = "form-control"
CHECK_CLASS = "form-check-input"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genre", "published_year", "available"]
        widgets = {
            "title": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "author": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "genre": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "published_year": forms.NumberInput(attrs={"class": INPUT_CLASS}),
            "available": forms.CheckboxInput(attrs={"class": CHECK_CLASS}),
        }
