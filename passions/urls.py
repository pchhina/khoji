from django.urls import path

from .views import PassionListView, PassionUpdateView, PassionCreateView

urlpatterns = [
    path("<int:pk>/edit/", PassionUpdateView.as_view(), name="passion_edit"),
    path("new/", PassionCreateView.as_view(), name="passion_new"),
    path("", PassionListView.as_view(), name="passion_list"),
]
