from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import GuestBook
from webapp.forms import GuestBookForm


def index_view(request):
    records = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'records': records
    }
    return render(request, 'index_view.html', context)


def create_record(request):
    if request.method == "GET":
        form = GuestBookForm()
        return render(request, "create_record.html", {'form': form})
    elif request.method == "POST":
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            GuestBook.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index_view')
        else:
            return render(request, 'create_record.html', {'form': form})


def update_record(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestBookForm(initial={
            'author': record.author,
            'email': record.email,
            'text': record.text
        })
        return render(request, 'update_record.html', {'form': form})
    elif request.method == "POST":
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data.get('author')
            record.email = form.cleaned_data.get('email')
            record.text = form.cleaned_data.get('text')
            record.save()
            return redirect('index_view')
        else:
            return render(request, 'update_record.html', {'form': form})


def delete_record(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        return render(request, "delete_record.html", {"record": record})
    elif request.method == "POST":
        record.delete()
        return redirect("index_view")
