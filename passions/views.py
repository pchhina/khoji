from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Passion, Goal

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


# Create your views here.
class GoalListView(ListView):
    model = Goal
    template_name = "goal_list.html"


class GoalUpdateView(UpdateView):
    model = Goal
    fields = (
        "name",
        "description",
        "target_finish_date",
        "members",
    )
    template_name = "goal_edit.html"
    success_url = reverse_lazy("goal_list")


class GoalCreateView(CreateView):
    model = Goal
    template_name = "goal_new.html"
    fields = (
        "name",
        "description",
        "owner",
        "target_start_date",
        "target_finish_date",
        "passion",
        "members",
    )
    success_url = reverse_lazy("goal_list")
