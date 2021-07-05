from django.shortcuts import render
from .  import models
from service  import models as models_service


def index(request):
    banner = models.Banner.objects.filter(status=True).first()
    categories = models_service.Categorie.objects.filter(status=True)
    return render(request, 'index.html', locals())


def category(request):
    categories = models_service.Categorie.objects.filter(status=True)
    services = models_service.Service.objects.filter(status=True)

    return render(request, 'category.html',locals())


def contact(request):
    return render(request, 'contact.html')


def listing(request):
    return render(request, 'listing.html')
# Create your views here.
