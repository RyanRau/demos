# CLAUDE.md — Library App

Local model agent. Follow tool rules strictly. Be terse.

## Structure
```
library/
  models.py
  views.py
  urls.py
  forms.py
  admin.py
  tests.py
  templates/
    library/
      base.html
      book_list.html
      book_detail.html
      book_form.html
      book_confirm_delete.html
  migrations/
  management/
  static/
  media/
library_demo/
  settings.py
  urls.py
manage.py
books_seed.csv
```

## Stack
Python 3.10+, Django 4.x, SQLite, Bootstrap 5 CDN. No third-party packages. No npm. No build steps.

## Conventions
- CBVs: ListView, DetailView, CreateView, UpdateView, DeleteView
- Forms: ModelForm in forms.py
- URL names: book-list, book-detail, book-create, book-update, book-delete
- Templates extend base.html
- App: `library` in INSTALLED_APPS

## Commands
```bash
python manage.py import_books books_seed.csv   # seed data
python manage.py import_books books_seed.csv --clear  # wipe then seed
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py test library.tests
python manage.py check
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

## Seed CSV format
```
title,author,genre,published_year,available
"1984","George Orwell","Science Fiction",1949,true
```
`available`: true/false (any case).

## Tool Rules
- One tool call at a time. Wait for result before next.
- Read file before editing. Never assume contents.
- Never invent file paths. List directory first if unsure.
- On tool failure: stop and report. Do not retry same call.
- Before creating a file: state path and purpose first.
- One bash command per call. No chaining.
- Makemigrations and migrate are always separate calls.
- Smallest possible edit. Preserve existing imports.
- Do not edit settings.py unless explicitly required.