from django.conf import settings
from website import models  as models_website


def website(request):

    website =   models_website.Website.objects.filter(status=True).first()
    config =   models_website.Configuration.objects.filter(status=True).first()

    return locals()