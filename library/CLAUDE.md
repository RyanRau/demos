# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

> **Note:** This agent is running on a local model. Follow the Tool Use Rules strictly to avoid errors.

---

## Project Overview

This is a Django CRUD application for managing a library book collection.
It uses Django's class-based views, SQLite, and Bootstrap 5 via CDN. Third-party packages are not used.

**Stack:** Python 3.10+, Django 4.x, SQLite, Bootstrap 5 (CDN)

### Project Structure

```
library/
  models.py          # Book model (and any related models)
  views.py           # CRUD views (class-based)
  urls.py            # App-level URL routing
  forms.py           # BookForm and any other forms
  admin.py           # Admin panel customization
  templates/
    base.html
    book_list.html
    book_detail.html
    book_form.html
    book_confirm_delete.html
  migrations/        # Database schema evolution history
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
# Create and apply database migrations (always as separate steps)
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test
python manage.py test library.tests  # single app

# Check for configuration issues
python manage.py check

# Create superuser for admin access
python manage.py createsuperuser

# Lint code
flake8 library/
```

> **Do not run `python manage.py runserver`** — it will hang the tool call indefinitely.

---

## Django Conventions in This Project

- Views are class-based (CBV): `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`
- Forms live in `forms.py` and use `ModelForm`
- URL names follow the pattern: `book-list`, `book-detail`, `book-create`, `book-update`, `book-delete`
- Templates extend `base.html` using `{% extends "base.html" %}`
- The app is named `library` and is registered in `INSTALLED_APPS`
- Database is SQLite — no external DB setup required
- Templates use Bootstrap 5 via CDN — do not add CSS frameworks, npm, or build steps

---

## Tool Use Rules

These rules exist because this agent is running on a local model. Follow them strictly.

### General

- **One tool call at a time.** Never chain or batch multiple tool calls in a single response. Wait for each result before proceeding.
- **Always read before writing.** Before editing any file, read it first so you have the current contents. Never assume file contents.
- **Never invent file paths.** Only reference files confirmed to exist. If unsure, list the directory first.
- **Do not retry a failed tool call with the same arguments.** Stop and explain the error instead.
- **State intent before creating new files.** Describe the intended path and purpose before writing.

### Bash / Shell

- **One command per bash call.** Do not chain with `&&`, `;`, or pipes except for standard Django idioms.
- **Migrations are always two separate steps:** `makemigrations` first, then `migrate`.
- **Never run `python manage.py runserver`.** It will hang.
- Prefer `python manage.py` commands over direct file manipulation where Django tooling applies.

### File Editing

- **Make the smallest possible edit.** Only change lines relevant to the task. Do not reformat unrelated code.
- **Preserve existing imports.** Append to the existing import block rather than rewriting it.
- **Do not touch `settings.py`** unless the task explicitly requires it.

### When Stuck

- If a tool call returns an unexpected result, stop and describe what happened rather than retrying or guessing.
- If unsure which file to edit, list the relevant directory first.
- If the task cannot be completed with available tools, say so clearly.