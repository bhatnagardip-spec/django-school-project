from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)


    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)
    Image = models.ImageField(upload_to='Items/')
   

class Slider(models.Model):
    description = models.TextField(blank=False)
    Image = models.ImageField(upload_to='Items/')
    Title = models.CharField(max_length=150)

class Testimonial(models.Model):
    description = models.TextField(blank=False)
    Image = models.ImageField(upload_to='Items/')
    name = models.CharField(max_length=25)

class ContactUs(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)

    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    footer_des = models.TextField(null=True, blank=True)
    temp = models.CharField(max_length=10, null=True, blank=True)