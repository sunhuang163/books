from django.db import models

# Create your models here.

class SiteCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="网站分类"

class Site(models.Model):

    name = models.CharField(max_length=200,verbose_name='网站名称')
    url = models.URLField(verbose_name="URL")
    category =models.ForeignKey(SiteCategory,related_name='site_category')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="网站设置"


class SiteRule(models.Model):
    sitename = models.ForeignKey(Site,related_name='site_name')
    rule = models.TextField()

    def __str__(self):
        return self.sitename.name

    class Meta:
        verbose_name_plural="网站规程"




