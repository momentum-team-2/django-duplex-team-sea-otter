from django import forms
from .models import Habit, DailyRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'goal_quantity',
            'goal',
            'unit_of_measure',
        ]




        