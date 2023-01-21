from django.urls import path

from .views import PassionListView, PassionUpdateView, PassionCreateView
from .views import GoalListView, GoalUpdateView, GoalCreateView

urlpatterns = [
    path("<int:pk>/edit/", PassionUpdateView.as_view(), name="passion_edit"),
    path("new/", PassionCreateView.as_view(), name="passion_new"),
    path("goals/", GoalListView.as_view(), name="goal_list"),
    path("goals/<int:pk>/edit/", GoalUpdateView.as_view(), name="goal_edit"),
    path("goals/new/", GoalCreateView.as_view(), name="goal_new"),
    path("", PassionListView.as_view(), name="passion_list"),
]
