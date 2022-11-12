from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import GuestBook


def index_view(request):
    records = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'records': records
    }
    return render(request, 'index_view.html', context)
