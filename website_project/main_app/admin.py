from django.contrib import admin
from .models import User, Uploader, ProjectMainModel, ProjectChildModel, CarouselModel, FrontModel, ProductModel
# Register your models here.

admin.site.register(User)
admin.site.register(Uploader)
admin.site.register(ProjectMainModel)
admin.site.register(ProjectChildModel)
admin.site.register(CarouselModel)
admin.site.register(FrontModel)
admin.site.register(ProductModel)

