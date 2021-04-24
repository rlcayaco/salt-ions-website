from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import User, ProjectMainModel, ProjectChildModel, Uploader, CarouselModel, FrontModel
from .forms import ProjectMainForm, ProjectChildForm, ProjectFrontForm, ProjectCarouselForm, CustomUserCreationForm

# For function based views
from django.contrib.auth.decorators import login_required
# For Class based views
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView,)

                                

# Django actually has a default UserCreateForm in
# from django.contrib.auth.forms import UserCreationForm
# but we choose to create our own here
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")

class LandingPageView(ListView):
    template_name = "landing_page.html"
    queryset = CarouselModel.objects.all()
    context_object_name = "carousel_list"

class CompanyProfileView(TemplateView):
    template_name = "company_profile.html"

class ContactUsView(TemplateView):
    template_name = "contact_us.html"


@login_required
def create_page(request):
    project_main = ProjectMainModel.objects.all()
    carousel_items = CarouselModel.objects.all()
    front_items = FrontModel.objects.all()

    context = {
        "project_main":project_main,
        "carousel_items":carousel_items,
        "front_items":front_items,
    }
    return render(request, "main_app/project_create.html", context)

# ====== Create | Main, Child, Front, Carousel ======
class CreateMainView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/create_main.html"
    form_class = ProjectMainForm
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class CreateChildView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/create_child.html"
    form_class = ProjectChildForm
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class CreateFrontView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/create_front.html"
    form_class = ProjectFrontForm
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class CreateCarouselView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/create_carousel.html"
    form_class = ProjectCarouselForm
    
    def get_success_url(self):
        return reverse("main_app:create_page")

# ====== Update/Delete Main & Child ======

class UpdateMainView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/update_main.html"
    queryset = ProjectMainModel.objects.all()
    form_class = ProjectMainForm
    context_object_name = "project_main"
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class DeleteMainView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/delete_main.html"
    queryset = ProjectMainModel.objects.all()
    context_object_name = "project_main"
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class CreateMainDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/create_main_detail.html"
    queryset = ProjectMainModel.objects.all()
    context_object_name = "create_main_detail"

class DeleteChildView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/delete_child.html"
    queryset = ProjectChildModel.objects.all()
    context_object_name = "project_child"

    def get_success_url(self):
        # project_main.pk is the Main pk=primarykey of the Child
        # You can also use project_main_id that is the name in the database itself
        # You can see this on the database
        return reverse("main_app:create_main_detail", kwargs={'pk': self.object.project_main.pk})


# ====== Update/Delete Carousel ======
class UpdateCarouselView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/update_carousel.html"
    queryset = CarouselModel.objects.all()
    form_class = ProjectCarouselForm
    context_object_name = "carousel"
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class DeleteCarouselView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/delete_carousel.html"
    queryset = CarouselModel.objects.all()
    context_object_name = "carousel"
    
    def get_success_url(self):
        return reverse("main_app:create_page")

# ====== Update/Delete Front ======
class UpdateFrontView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/update_front.html"
    queryset = FrontModel.objects.all()
    form_class = ProjectFrontForm
    context_object_name = "front"
    
    def get_success_url(self):
        return reverse("main_app:create_page")

class DeleteFrontView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'main_app/project_create.html'

    template_name = "main_app/delete_front.html"
    queryset = FrontModel.objects.all()
    context_object_name = "front"
    
    def get_success_url(self):
        return reverse("main_app:create_page")




def landing_page(request):
    carousel = CarouselModel.objects.all()
    front_obj = FrontModel.objects.all()

    context = {
        "carousel":carousel,
        "front_obj":front_obj,
    }
    return render(request, "landing_page.html", context)


def contact(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send the email
        send_mail(
            subject="Website Email",
            message="Sender Name: " + message_name + "\n" + "Sender Message: " + message + "\n" + "Sender Email: " + message_email,

            # When you send emails through google's SMTP servers you cannot change the from email field.
            # It uses the same address that you provided for authentication.
            from_email="",
            recipient_list=['ionssalt@gmail.com'],
            fail_silently=False,
        )

        return render(request, "contact_us.html", context={'message_name':message_name})
    else:
        return render(request, "contact_us.html", context={})


class ProjectListView(ListView):
    template_name = "main_app/project_list.html"
    queryset = ProjectMainModel.objects.all()
    context_object_name = "project_list"

class ProjectDetailView(DetailView):
    template_name = "main_app/project_detail.html"
    queryset = ProjectMainModel.objects.all()
    context_object_name = "project_detail"









# def project_list(request):
#     # This returns a queryset
#     projects = Project.objects.all()
#     context = {
#         "projects": projects,
#     }
#     return render(request, 'main_app/project_list.html', context)

# def project_detail(request, pk):
#     project = Project.objects.get(id=pk)
#     context = {
#         "project":project,
#     }
#     return render(request, 'main_app/project_detail.html', context)

# def project_create(request):
#     print(request.POST)
#     form = Project_form()
#     context = {
#         "form":form
#     }
#     return render(request, 'main_app/project_create.html', context)