from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .forms import GoalForm, DailyForm
from .models import Goal, Daily
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('stamps:calendar')
    else:
        form = GoalForm()
    context = {
        'form': form,
    }
    return render(request, 'stamps/create.html', context)



@require_safe
def calendar(request):
    daily_form = DailyForm()
    context = {
        'daily_form': daily_form,
    }
    return render(request, 'stamps/calendar.html', context)

@require_POST
def create_daily(request, goal_pk):
    if request.user.is_authenticated:
        goal = get_object_or_404(klass=Goal, pk=goal_pk)
        form = DailyForm(request.POST)
        if form.is_valid():
            daily = form.save(commit=False)
            daily.user = request.user
            daily.goal = goal
            daily.save()
            return redirect('stamps:calendar')