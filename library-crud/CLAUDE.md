# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This is a Django CRUD application for managing a library book collection. It uses Django's class-based views, SQLite, and Bootstrap 5 via CDN. Third-party packages are not used.

**Stack:** Python 3.10+, Django 4.x, SQLite, Bootstrap 5 (CDN)

### Project Structure

```
library/
  models.py          # Book model (and any related models)
  views.py           # CRUD views (class-based)
  urls.py            # App-level URL routing
  forms.py           # BookForm and any other forms
  admin.py           # Admin panel customization
  tests.py           # Unit tests for models/views
  templates/
    library/         # App-specific templates
      base.html
      book_list.html
      book_detail.html
      book_form.html
      book_confirm_delete.html
  migrations/        # Database schema evolution history
  management/        # Custom management commands
  static/            # Static files (CSS, JS)
  media/             # User-uploaded files
library_demo/
  settings.py        # Development settings (DEBUG=True, SQLite)
  urls.py            # Root URL configuration
manage.py
```

The project follows standard Django patterns:
- Model-View-Template (MVT) architecture
- Convention-over-configuration for URL routing
- Built-in admin panel for data management

---

## Common Development Commands

```bash
# Import books from CSV (with optional --clear flag to reset database)
python manage.py import_books books_seed.csv --clear

# Create and apply database migrations (always as separate steps)
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test
python manage.py test library.tests  # single app tests

# Check for configuration issues
python manage.py check

# Create superuser for admin access
python manage.py createsuperuser

# Lint code
flake8 library/

# Collect static files (if needed)
python manage.py collectstatic --noinput
```

```bash
# Import books from CSV (with optional --clear flag to reset database)
python manage.py import_books books_seed.csv --clear

# ... existing commands below ...

```bash
# Create and apply database migrations (always as separate steps)
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test
python manage.py test library.tests  # Single app tests

# Check for configuration issues
python manage.py check

# Create superuser for admin access
python manage.py createsuperuser

# Lint code
flake8 library/

# Collect static files (if needed)
python manage.py collectstatic --noinput
```

> **Do not run `python manage.py runserver`** — it will hang the tool call indefinitely.

---

## Django Conventions in This Project

- **Data Seeding**: The `import_books` management command is used to populate the database from `books_seed.csv`. The CSV must contain these columns in order: `title,author,genre,published_year,available`. The `available` field accepts boolean values (true/false) in any case.

- **Views**: Class-based (CBV): `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`
- **Forms**: Live in `forms.py` and use `ModelForm`
- **URL Routing**: Names follow `book-list`, `book-detail`, `book-create`, `book-update`, `book-delete`
- **Templates**: Extend `base.html` using `{% extends "base.html" %}`
- **App Configuration**: App is named `library` and registered in `INSTALLED_APPS`
- **Database**: SQLite — no external DB setup required
- **Frontend**: Bootstrap 5 via CDN — no npm or build steps allowed

---

## Tool Use Rules

- **Data Seeding**: When using the `import_books` command, ensure the `books_seed.csv` file exists and is correctly formatted. The CSV must have these columns in order: `title,author,genre,published_year,available`. The `available` field accepts boolean values (true/false) in any case. Use the `--clear` flag to delete existing books before import if needed.

These rules exist because this agent is running on a local model. Follow them strictly.

### General

- **One tool call at a time.** Never chain or batch multiple tool calls in a single response.
- **Always read before writing.** Before editing any file, read it first to confirm contents.
- **Never invent file paths.** Only reference files confirmed to exist.
- **Do not retry a failed tool call with the same arguments.** Stop and explain the error.
- **State intent before creating new files.** Describe the intended path and purpose before writing.

### Bash / Shell


- **One command per bash call.** Do not chain with `&&`, `;`, or pipes except for standard Django idioms.
- **Migrations are always two separate steps:** `makemigrations` first, then `migrate`.
- **Never run `python manage.py runserver`.** It will hang.
- Prefer `python manage.py` commands over direct file manipulation where Django tooling applies.

### File Editing

- **Make the smallest possible edit.** Only change lines relevant to the task.
- **Preserve existing imports.** Append to the existing import block rather than rewriting it.
- **Do not touch `settings.py`** unless the task explicitly requires it.

---

## High-Level Architecture

This Django project follows a classic MVT pattern:

- **Data Seeding**: Uses a custom management command `import_books` to populate the database from a CSV file (`books_seed.csv`). The command supports a `--clear` flag to delete existing books before import. Expected CSV format:
  ```csv
  title,author,genre,published_year,available
  "To Kill a Mockingbird","Harper Lee","Classic",1960,true
  "1984","George Orwell","Science Fiction",1949,true
  # ... additional entries
  ```

- **Models**: `Book` model in `models.py` with fields matching the CSV structure (title, author, genre, published_year, available). The `available` field is stored as a boolean.

1. **Models** (`models.py`): Define the `Book` data structure with fields like title, author, ISBN, etc.
2. **Views** (`views.py`): Use class-based views to handle CRUD operations, leveraging Django's generic views.
3. **URL Routing** (`urls.py`): Maps URLs to views using Django's `path()` and `include()`.
4. **Templates** (`templates/`): Bootstrap 5 HTML templates that extend `base.html` for consistent styling.
5. **Admin Panel** (`admin.py`): Registers models with the Django admin for quick data management.

**Request Flow**:
User → URLconf → View → Model/Template → Response

**Database**: SQLite is used for development, with migrations managed through Django's ORM.

---

## Testing Strategy


- **Test Location**: `library/tests.py` contains test cases for models and views.
- **Test Types**: Unit tests for model validation and view behavior (e.g., form submission, template rendering).
- **Running Tests**: Use `python manage.py test` for full test suite or specify individual test modules.

---

## Security Considerations

- **CSRF Protection**: Django's built-in CSRF middleware is enabled by default.
- **Admin Security**: Superuser credentials should be stored securely, not in version control.
- **Input Validation**: Forms use Django's `ModelForm` to enforce field constraints and validation.

---

## Future Enhancements


This document should be updated if:
- New apps are added to the project
- Third-party packages are introduced
- Frontend build steps are added (unlikely due to Bootstrap CDN usage)
- Database backend changes (e.g., PostgreSQL in production)