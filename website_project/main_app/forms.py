from django import forms 
from .models import ProjectMainModel, ProjectChildModel, FrontModel, CarouselModel, ProductModel
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import get_user_model

# get_user_model() Returns the User model that is active in this project.
# User = get_user_model()

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}


class ProjectMainForm(forms.ModelForm):
    class Meta:
        model = ProjectMainModel
        fields = [
            'project_main_name',
            'project_main_image',
        ]
        widgets = {
            'project_main_name':forms.TextInput(attrs={'placeholder':'Main Name'})
        }

class ProjectChildForm(forms.ModelForm):
    class Meta:
        model = ProjectChildModel
        fields = [
            'project_child_name',
            'project_child_image',
            'project_main',
        ]
        widgets = {
            'project_child_name':forms.TextInput(attrs={'placeholder':'Child Name'})
        }

class ProjectFrontForm(forms.ModelForm):
    class Meta:
        model = FrontModel
        fields = [
            'front_name',
            'front_image',
            'front_main',
        ]
        widgets = {
            'front_name':forms.TextInput(attrs={'placeholder':'Front Name'})
        }       

class ProjectCarouselForm(forms.ModelForm):
    class Meta:
        model = CarouselModel
        fields = [
            'carousel_name',
            'carousel_image',
        ]
        widgets = {
            'carousel_name':forms.TextInput(attrs={'placeholder':'Carousel Name'})
        }  

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            'product_name',
            'project_image',
            'product_description',
        ]
        widgets = {
            'product_name':forms.TextInput(attrs={'placeholder':'Product Name'}),
            'product_description':forms.TextInput(attrs={'placeholder':'Description'}),
        }  