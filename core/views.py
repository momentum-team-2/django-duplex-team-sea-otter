from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Habit
from .forms import HabitForm

# Create your views here.
def list_habits(request):
    habits = Habit.objects.order_by('-id')
    return render(request, 'habits/list_habits.html', {'habits': habits})


def show_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    form = HabitForm()
    return render(request, 'habits/show_habits.html', {'habit': habit, 'pk': pk, 'form': form})


def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, 'habits/add_habit.html', {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')
    return render(request, 'habits/edit_habit.html', {'form': form, 'habit': habit})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        messages.success(request, 'Habit deleted.')
        return redirect(to='list_habits')
    return render(request, 'habits/delete_habits.html', {'habit': habit})