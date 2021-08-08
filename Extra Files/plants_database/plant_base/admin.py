from django.contrib import admin

from .models import Plants, Flowers, Leaves, Berries, Stems

admin.site.register(Plants)
admin.site.register(Berries)
admin.site.register(Flowers)
admin.site.register(Leaves)
admin.site.register(Stems)
