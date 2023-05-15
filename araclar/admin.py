from django.contrib import admin
from .models import araclar,marka

@admin.register(araclar)
class AracAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","slug","marka_listele",)
    list_display_links= ("title","slug",)
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title","isActive","isHome")
    list_editable = ("isActive","isHome",)
    search_fields = ("title","description")

    def marka_listele(self, obj):
        html = ""
        for marka in obj.marka.all():
            html += marka.name + " "
        return html


@admin.register(marka)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ("name","slug","arac_sayisi")
    prepopulated_fields = {"slug": ("name",),}

    def arac_sayisi(self,obj):
        return obj.araclar_set.count()