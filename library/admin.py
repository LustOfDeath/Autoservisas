from django.contrib import admin
from .models import Automobilis, AutomobilisModelis, Paslauga, Uzsakymas, UzsakymoEilute


class UzsakymoEiluteInLine(admin.TabularInline):
    model = UzsakymoEilute
    readonly_fields = ('id',)
    extra = 0


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilis_id', 'valstybinis_nr', 'vin_kodas')
    search_fields = ('valstybinis_nr', 'vin_kodas')
    list_filter = ('klientas', 'automobilis_id')


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis', 'atsiemimo_data')
    inlines = [UzsakymoEiluteInLine]


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(AutomobilisModelis)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)
