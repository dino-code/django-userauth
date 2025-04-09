#%% md
# Django User Authentication Practice Project

## Overview
This is a practice project developed to learn and understand Django's user registration and authentication flow. The project implements core authentication features including user registration, login, logout, and profile management.

## Purpose
The main purpose of this project is educational - to gain hands-on experience with Django's built-in authentication system and customize it for specific needs. This project serves as a learning tool for understanding how user authentication works in Django web applications.

## Features
- User registration with form validation
- User login and authentication
- User logout functionality
- User profile management
- Secured views that require authentication

## Project Structure
The project consists of a main Django project (`userauth`) with an `accounts` app that handles all authentication-related functionality.

### Main Components:
- **accounts/views.py**: Contains view functions for registration, login, profile pages
- **accounts/forms.py**: Custom forms for user registration and authentication
- **accounts/urls.py**: URL patterns for authentication routes
- **accounts/templates**: HTML templates for auth-related pages
- **templates/base.html**: Base template used throughout the application

## Technologies Used
- Django Framework
- SQLite database (for development)
- Django's built-in authentication system
- HTML/CSS for templates

## Learning Objectives
- Understanding Django's authentication system
- Implementing custom user registration forms
- Managing user sessions
- Protecting views with authentication requirements
- Following Django best practices for user authentication

## Getting Started

### Prerequisites
- Python 3.x
- Django

### Installation
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`

## Note
This is a practice project and not intended for production use. It serves as a learning resource for Django's authentication system.