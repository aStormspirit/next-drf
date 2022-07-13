from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Products(models.Model):
    id = models.IntegerField(_('id'),primary_key=True)
    article = models.IntegerField(_('article'))
    name = models.CharField(_("name"),max_length=64)
    description = models.TextField(_("description"))
    price = models.IntegerField(_('price'))
    category = models.CharField(_("category"),max_length=64)
    image = models.URLField(_("image"),max_length=300)

    def __str__(self):
        return self.name
