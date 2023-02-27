from django import forms

from .models import PassionComment
from .models import GoalComment


class PassionCommentForm(forms.ModelForm):
    class Meta:
        model = PassionComment
        fields = ("comment", "author")


class GoalCommentForm(forms.ModelForm):
    class Meta:
        model = GoalComment
        fields = ("comment", "author")
