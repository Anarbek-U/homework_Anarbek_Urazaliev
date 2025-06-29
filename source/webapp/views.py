
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('-created_at')
    if request.method == "POST":
        task_ids = request.POST.getlist('task_ids')
        if task_ids:
            Task.objects.filter(id__in=task_ids).delete()
            return redirect('index')
    else:
        return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get('description')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')
        more_detailed = request.POST.get('more_detailed')
        Task.objects.create(description=description, status=status, created_at=created_at, more_detailed=more_detailed)
        return redirect('index')
    else:
        return render(request, 'create_task.html', {"status_choices": status_choices})

def detail_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    all_tasks = Task.objects.order_by('-created_at')
    task_num = list(all_tasks).index(task) + 1
    if request.method == "POST":
        task.delete()
        return redirect('index')
    else:
        return render(request, 'detailed_task.html', {"task": task, "task_num": task_num})




