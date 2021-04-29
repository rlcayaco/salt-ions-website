from django.urls import path
from main_app.views import ( ProjectListView, ProjectDetailView, create_page, 
                                CreateMainView, CreateChildView, CreateFrontView, 
                                CreateCarouselView, UpdateMainView, DeleteMainView, 
                                CreateMainDetailView, DeleteChildView, UpdateCarouselView,
                                DeleteCarouselView, UpdateFrontView, DeleteFrontView,
                                CreateProductView, UpdateProductView, DeleteProductView )


app_name = 'main_app'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/create_main_detail/', CreateMainDetailView.as_view(), name='create_main_detail'),
    path('<int:pk>/update/', UpdateMainView.as_view(), name='update_main'),
    path('<int:pk>/update_carousel/', UpdateCarouselView.as_view(), name='update_carousel'),
    path('<int:pk>/update_product/', UpdateProductView.as_view(), name='update_product'),
    path('<int:pk>/update_front/', UpdateFrontView.as_view(), name='update_front'),
    path('<int:pk>/delete/', DeleteMainView.as_view(), name='delete_main'),
    path('<int:pk>/delete_carousel/', DeleteCarouselView.as_view(), name='delete_carousel'),
    path('<int:pk>/delete_front/', DeleteFrontView.as_view(), name='delete_front'),
    path('<int:pk>/delete_child/', DeleteChildView.as_view(), name='delete_child'),
    path('<int:pk>/delete_product/', DeleteProductView.as_view(), name='delete_product'),
    path('create/', create_page, name='create_page'),
    path('create/create_main/', CreateMainView.as_view(), name='create_main' ),
    path('create/create_child/', CreateChildView.as_view(), name='create_child' ),
    path('create/create_front/', CreateFrontView.as_view(), name='create_front' ),
    path('create/create_carousel/', CreateCarouselView.as_view(), name='create_carousel' ),
    path('create/create_product/', CreateProductView.as_view(), name='create_product' ),
]


