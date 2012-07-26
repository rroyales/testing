from django.contrib import admin
from beer.models import Beer, Brewery

class BeerAdmin(admin.ModelAdmin):

		prepopulated_fields = {'slug':('name',)} # automatically make a slug name from the name input,
		# uncomment to use fieldsets, too much work only needed for design
		#fieldsets = [
        #(None,               {'fields': ['name']}),
        #('Beer Description', {'fields': ['slug', 'description'],'classes': ['collapse']}),
		#('Location', {'fields': ['brewery', 'locality'],'classes': ['collapse']}),
		
    #]
		#fields = ['name', 'slug', 'brewery', 'locality', 'description',]
		list_display = ('name', 'slug', 'brewery', 'locality', 'description',) # make a table inside admin
		search_fields = ['name']
class BreweryAdmin(admin.ModelAdmin):
		prepopulated_fields = {'slug':('name',)}
		
admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery, BreweryAdmin) 