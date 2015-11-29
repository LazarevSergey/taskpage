from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import auth
from upp_app.models import Section, TaskInSection, Task, UserPickedTask, Submission
import task_library.task_reader


def task_page(request, section_id, task_id):
    if not request.user.is_authenticated():
        return redirect('access')
    else:
        if UserPickedTask.Objects.all().filter(id_section=section_id, id_user=User.Objects.all().filter(username=auth.get_user(request))) == None:
            if Submission.Objects.all().filter(id_section=section_id, id_user=User.Objects.all().filter(username=auth.get_user(request)), id_task=task_id) == None:
                return redirect('access')
            else:
                return render(request, 'task_page/task_page_close.html')
        else:
            tasks = {}
            for i in task_id:
                task = get_object_or_404(Task, id=i.id)
                tasks[task_library.task_reader.get_task_html(task.id)] = task_library.task_reader.get_tutorial_html(
                    task.id)
            context = {}
            context['tasks'] = tasks
            context['section'] = get_object_or_404(Section, id=section_id)
            return render(request, 'task_page/task_page_open.html', context)