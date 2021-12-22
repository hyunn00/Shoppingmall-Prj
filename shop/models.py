from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta :
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self) :
        return reverse('shop:products_by_category', args = [self.slug])
    
    def __str__(self) :
        return '{}'.format(self.name)
    
class Product(models.Model) :
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to = 'product', blank = True)

    class Meta :
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def get_url(self) :
        return reverse('shop:ProdCatDetail', args = [self.category.slug, self.slug])
    
    def __str__(self) :
        return self.name