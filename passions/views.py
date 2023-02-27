from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Passion, Goal
from .forms import PassionCommentForm, GoalCommentForm

# Create your views here.


class PassionCommentGet(DetailView):
    model = Passion
    template_name = "passion_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PassionCommentForm()
        return context


class PassionCommentPost(SingleObjectMixin, FormView):
    model = Passion
    form_class = PassionCommentForm
    template_name = "passion_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.passion = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        passion = self.get_object()
        return reverse("passion_detail", kwargs={"pk": passion.pk})


class PassionDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = PassionCommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PassionCommentPost.as_view()
        return view(request, *args, **kwargs)


class PassionListView(ListView):
    model = Passion
    template_name = "passion_list.html"


class PassionUpdateView(UpdateView):
    model = Passion
    fields = (
        "name",
        "description",
        "members",
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
        "members",
    )
    success_url = reverse_lazy("passion_list")


# Create your views here.
class GoalCommentGet(DetailView):
    model = Goal
    template_name = "goal_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GoalCommentForm()
        return context


class GoalCommentPost(SingleObjectMixin, FormView):
    model = Goal
    form_class = GoalCommentForm
    template_name = "goal_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.goal = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        goal = self.get_object()
        return reverse("goal_detail", kwargs={"pk": goal.pk})


class GoalDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = GoalCommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = GoalCommentPost.as_view()
        return view(request, *args, **kwargs)


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
