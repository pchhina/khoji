from django.urls import path

from .views import (
    PassionDetailView,
    PassionListView,
    PassionUpdateView,
    PassionCreateView,
)
from .views import GoalDetailView, GoalListView, GoalUpdateView, GoalCreateView

urlpatterns = [
    path("<int:pk>/", PassionDetailView.as_view(), name="passion_detail"),
    path("<int:pk>/edit/", PassionUpdateView.as_view(), name="passion_edit"),
    path("new/", PassionCreateView.as_view(), name="passion_new"),
    path("goals/", GoalListView.as_view(), name="goal_list"),
    path("goals/<int:pk>/", GoalDetailView.as_view(), name="goal_detail"),
    path("goals/<int:pk>/edit/", GoalUpdateView.as_view(), name="goal_edit"),
    path("goals/new/", GoalCreateView.as_view(), name="goal_new"),
    path("", PassionListView.as_view(), name="passion_list"),
]
