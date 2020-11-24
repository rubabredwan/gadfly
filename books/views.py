from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def available_books_view(request):
  if request.method == 'GET':
    Books = Book.objects.all()
    return render(request, 'show_all.html', {'books': Books})

def add_new_view(request):
  if request.method == 'POST':
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('success')
  else:
    form = BookForm()
  return render(request, 'add_new.html', {'form': form})

def success(request):
  return HttpResponse('Successfully uploaded')

