from django.conf import settings
from django.http import HttpResponse
from .models import URL
from django.template import loader

def viihde(request):
	site = loader.get_template('viihdeAPI/index.html')
	return HttpResponse(site.render({'API_URL': settings.API_URL, 'DEPENDENCY_URL': settings.DEPENDENCY_URL}, request))

def streamURL(request):
	q = request.GET.get('q').lower()
	return HttpResponse(e.url for e in URL.objects.filter(query=q))
