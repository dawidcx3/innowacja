from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Cat

class CatAdmin(admin.ModelAdmin):
    readonly_fields = ('gender',)
    
admin.site.register(Cat, CatAdmin)

from .models import Color

admin.site.register(Color)

from .models import Prey

admin.site.register(Prey)

from .models import Hunting

admin.site.register(Hunting)

from .models import Usr

admin.site.register(Usr)