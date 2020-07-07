from django import forms
from .models import Habit, Record

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'goal_quantity',
            'goal',
            'unit_of_measure',
        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'quantity',
            'unit_of_measure'
        ]




        