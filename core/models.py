from django.db import models


options = [["F", "Femenino"], ["M", "Masculino"]]

option_civil_status = [
    ["CA", "Casad@"],
    ["DI", "Divorciad@"],
    ["VI", "Viud@"],
    ["UL", "Union libre"],
]


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=200, verbose_name="Apellidos")
    sex = models.CharField(choices=options, verbose_name="Sexo")
    civil_status = models.CharField(choices=option_civil_status)
    address = models.CharField(max_length=100, verbose_name="Direccion")
    comment = models.TextField()
    
    def __str__(self) -> str:
        return  self.name
    
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        db_table = 'usuario'
        ordering = ['id'] 
        

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return  self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'
        ordering = ['id'] 


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=9)
    descitption = models.CharField(max_length=255, default='', blank=True, null=True)
    img = models.ImageField(upload_to='img_servicios/',blank=True, null=True)
    # Add parametros de venta
    sale = models.BooleanField(default=False)
    sale_prace = models.DecimalField(default=0, decimal_places=0, max_digits=8)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        db_table = 'servicio'
        ordering = ['id'] 