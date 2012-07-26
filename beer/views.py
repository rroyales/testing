from django.template import RequestContext
from django.shortcuts import render_to_response
from beer.models import Beer, Brewery

def BeersAll(request):
		vBeer = Beer.objects.all().order_by('name')
		context = {'beers': vBeer}
		return render_to_response('beers/beersall.html', context, context_instance=RequestContext(request))
		
def SpecificBeer(request, beerslug):
		vBeer = Beer.objects.get(slug=beerslug)
		context = {'beers': vBeer}
		return render_to_response('beers/singlebeer.html', context, context_instance=RequestContext(request))
		
def SpecificBrewery(request, breweryslug):
		vbrewery = Brewery.objects.get(slug=breweryslug)
		vBeer = Beer.objects.filter(brewery=vbrewery)
		context = {'beers': vBeer}
		return render_to_response('beers/specificbrewery.html', context, context_instance=RequestContext(request))