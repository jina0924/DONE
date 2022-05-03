from django import forms
from .models import Goal, Daily

from datetime import datetime, timedelta
now = datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nextMonth = (now + timedelta(weeks=4)).strftime('%Y-%m-%d')
tomorrow = (now + timedelta(days=1)).strftime('%Y-%m-%d')

class GoalForm(forms.ModelForm):
    start_date = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date',
                'value': nowDate,
                'min': nowDate,
                'class': 'start-date-form form-control',
            }
        )
    )
    
    end_date = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date',
                'value': nextMonth,
                'min': tomorrow,
                'class': 'end-date-form form-control',
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'목표를 작성해주세요!'
            }
        )
    )

    target_amount = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':'목표 횟수를 설정해주세요!'
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