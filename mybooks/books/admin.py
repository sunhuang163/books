from django.contrib import admin
from  .models import Site,SiteCategory,SiteRule
# Register your models here.

admin.site.register(Site)
admin.site.register(SiteCategory)
admin.site.register(SiteRule)
