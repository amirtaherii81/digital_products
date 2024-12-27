from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_("parent"), on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    avatar = models.ImageField(_("Avatar"), upload_to="cotegories", null=True, blank=True)
    is_active = models.BooleanField(_("Is active?"), default=True)
    create_time = models.DateTimeField(_("Create Time"), auto_now_add=True)
    update_time = models.DateTimeField(_("Update Time"), auto_now=True)

    class Meta:
        db_table = "categorie"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"), blank=True)
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    avatar = models.ImageField(_("Avatar"), upload_to="products", null=True, blank=True)
    is_active = models.BooleanField(_("Is active?"), default=True)
    create_time = models.DateTimeField(_("Create Time"), auto_now_add=True)
    update_time = models.DateTimeField(_("Update Time"), auto_now=True)

    class Meta:
        db_table = "product"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class File(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=100)
    file = models.FileField(_("File"), upload_to="files/%Y/%m/%d",)
    is_active = models.BooleanField(_("Is active?"), default=True)
    create_time = models.DateTimeField(_("Create Time"), auto_now_add=True)
    update_time = models.DateTimeField(_("Update Time"), auto_now=True)

