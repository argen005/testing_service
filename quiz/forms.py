from django import forms
from .models import Answer

class AnswerForm(forms.Form):
    answers = forms.ModelMultipleChoiceField(queryset=Answer.objects.all(), widget=forms.CheckboxSelectMultiple)
