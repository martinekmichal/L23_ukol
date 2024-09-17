from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Data
from .forms import FotoForm


class UserListView(ListView):
    model = Data
    template_name = 'user_list.html'


class UserFotoView(DetailView):
    model = Data
    template_name = 'user_foto.html'


class CreateFotoView(CreateView):
    model = Data
    form_class = FotoForm
    template_name = 'create_foto.html'
    success_url = reverse_lazy('user_list')