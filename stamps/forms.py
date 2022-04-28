from django import forms
from .models import Goal, Daily

class GoalForm(forms.ModelForm):
    start_date = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    end_date = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Goal
        exclude = ['user',]




class DailyForm(forms.ModelForm):

    class Meta:
        model = Daily
        exclude = ['user', 'goal',]