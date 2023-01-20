from django.shortcuts import render
from .models import Contact

def index(request):
    search = request.GET.get('search', '')
    contacts = Contact.objects.filter(
            name__icontains=search)
    context = {
            'contacts': contacts
            }
    return render(request, 'contact/index.html', context)
