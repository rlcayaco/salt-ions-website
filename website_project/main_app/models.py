from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class ProjectMainModel(models.Model):
    project_main_name = models.CharField(max_length=60)
    project_main_image = models.ImageField(upload_to="project_images/main_images/", default="placeholder-image.png")

    def __str__(self):
        return self.project_main_name

class ProjectChildModel(models.Model):
    project_child_name = models.CharField(max_length=60)
    project_child_image = models.ImageField(upload_to="project_images/child_images/", default="placeholder-image.png")
    project_main = models.ForeignKey(ProjectMainModel, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.project_child_name

class FrontModel(models.Model):
    front_name = models.CharField(max_length=60)
    front_image = models.ImageField(upload_to="project_images/front_images/", default="placeholder-image.png")
    front_main = models.ForeignKey(ProjectMainModel, on_delete=models.CASCADE, related_name='front')

    def __str__(self):
        return self.front_name

class Uploader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        
class CarouselModel(models.Model):
    carousel_name = models.CharField(max_length=60)
    carousel_image = models.ImageField(upload_to="project_images/carousel_images/", default="placeholder-image.png")

    def __str__(self):
        return self.carousel_name

class ProductModel(models.Model):
    product_name = models.CharField(max_length=60)
    project_image = models.ImageField(upload_to="product_images/", default="placeholder-image.png")
    product_description = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name