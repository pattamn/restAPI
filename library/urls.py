"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .views import *
urlpatterns = [
    path('libraries/up-sert', lib_upsert),
    path('libraries/get/all',lib_getAll),
    path('libraries/get/<lib_id>',lib_get),

    path('books/up-sert', books_upsert),
    path('books/get/all',books_getAll),
    path('books/get/<book_id>',books_get),

    path('library_book/get/library/<library_id>/check-out', library_book_get_checkout_bylibrary),
    path('library_book/get/user/<user_id>/check-out', library_book_get_checkout_byuser),

    path('library_book/<library_id>/up-sert', library_book_create),
    path('library_book/<book_id>/<user_id>/up-sert/check-out', library_book_checkout),
    path('library_book/<book_id>/<user_id>/up-sert/check-in', library_book_checkin),

]
