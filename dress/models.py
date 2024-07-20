from django.db import models

class  Model(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Dress(models.Model):
    title = models.CharField(max_length=32)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    CHOICES_COLLECTION = (
        ('Женское', 'Женское'),
        ('Мужское', 'Мужское')
    )
    collections = models.CharField(max_length=16, choices=CHOICES_COLLECTION)

    def __str__(self):
        return self.title

class DressPhoto(models.Model):
       image = models.ImageField(upload_to='img/', null=True,blank=True)
       dress = models.ForeignKey(Dress,on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.CharField(max_length=16)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} : {self.dress}'