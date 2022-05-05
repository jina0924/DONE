from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .forms import GoalForm, DailyForm
from .models import Goal, Daily
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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


def calendars(request):
    goals = Goal.objects.all()
    context = {
        'goals':goals,
    }
    return render(request, 'stamps/calendars.html', context)


@require_safe
def api(request):
    if request.user.is_authenticated:
        goals = Goal.objects.all()
        goals_json = []

        for goal in goals:
            goals_json.append({
                'id': goal.pk,
                'content': goal.content,
                'target_amount': goal.target_amount,
                'start_date': goal.start_date,
                'end_date': goal.end_date,
            })
        return JsonResponse(goals_json, safe=False)
    return redirect('accounts:login')



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