from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
import datetime
from .forms import HabitForm, RecordForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('list_habits')
    return render(request, 'habits/home.html')

@login_required
def list_habits(request):
    habits = request.user.habits.all()
    return render(request, 'habits/list_habits.html', {'habits': habits})

@login_required
def show_habit(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)
    form = HabitForm()
    records = habit.records.order_by('recorded_on')
    return render(request, 'habits/show_habit.html', {'habit': habit, 'pk': pk, 'form': form, 'records': records})

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='list_habits')
    else:
        form = HabitForm()

    return render(request, 'habits/add_habit.html', {'form': form})


@login_required
def add_record(request, pk, month=None, day=None,  year=None,):
    habit = get_object_or_404(request.user.habits, pk=pk)
    records = habit.records.order_by('-recorded_on')
    if year is None:
        record_date = datetime.date.today()
    else:
        record_date = datetime.date(year, month, day)
    
    next_day = record_date + datetime.timedelta(days=1)
    prev_day = record_date - datetime.timedelta(days=1)
    record = habit.records.filter(recorded_on=record_date).first()

    if record is None:
        record = Record(habit=habit, recorded_on=record_date)

    if request.method == 'POST':
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='show_habit', pk=pk)
    else:
        form = RecordForm(instance=record)

    return render(request, 'habits/add_record.html', {'form': form, 'habit': habit, 'date': record_date, 'next_day': next_day, 'prev_day': prev_day, 'record': record,})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)
    if request.method == 'POST':
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            habit = form.save()
            return redirect(to='list_habits')
    else:
        form = HabitForm(instance=habit)

    return render(request, 'habits/edit_habit.html', {'form': form, 'habit': habit})

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)
    if request.method == 'POST':
        habit.delete()
        messages.success(request, 'Habit deleted.')
        return redirect(to='list_habits')
        
    return render(request, 'habits/delete_habit.html', {'habit': habit})