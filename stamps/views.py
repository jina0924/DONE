from django.shortcuts import redirect, render
from .forms import GoalForm, DailyForm
from django.views.decorators.http import require_http_methods, require_safe

# Create your views here.
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
    return render(request, 'stamps/calendar.html')
