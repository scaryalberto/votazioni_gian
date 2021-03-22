from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import CandidatiUomo, CandidatiDonna


class CandidatiDonnaAdmin(admin.ModelAdmin):
    exclude=("votes",)
    readonly_fields=('votes', )

class CandidatiUomoAdmin(admin.ModelAdmin):
    exclude=("votes",)
    readonly_fields=('votes', )





admin.site.register(CandidatiDonna, CandidatiDonnaAdmin)#post è il modello che abbiamo creato... stiamo dicendo a django: rendilo disponibile per admnin
admin.site.register(CandidatiUomo, CandidatiUomoAdmin)#post è il modello che abbiamo creato... stiamo dicendo a django: rendilo disponibile per admnin