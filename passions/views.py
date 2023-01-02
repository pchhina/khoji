from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Passion

# Create your views here.
class PassionListView(ListView):
    model = Passion
    template_name = "passion_list.html"


class PassionUpdateView(UpdateView):
    model = Passion
    fields = (
        "name",
        "description",
    )
    template_name = "passion_edit.html"
    success_url = reverse_lazy("passion_list")


class PassionCreateView(CreateView):
    model = Passion
    template_name = "passion_new.html"
    fields = (
        "name",
        "description",
        "owner",
    )
    success_url = reverse_lazy("passion_list")