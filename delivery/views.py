from django.views import generic
from .models import DeliveryTask
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib import messages


# views related to delivery manager
class AllTasksView(generic.ListView):
    model=DeliveryTask
    template_name = 'delivery/manager.html'



def task_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('login_user')
    else:
        user = request.user
        task = get_object_or_404(DeliveryTask, pk=pk)
        return render(request, 'delivery/task_detail.html', {'task': task, 'user': user})



class TaskCreate(CreateView):
    model = DeliveryTask
    fields = ['title','priority']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        temp_priority =self.request.POST['priority']
        final_priority=1
        if temp_priority.upper()=="LOW":
            final_priority=1
        elif temp_priority.upper()=="MEDIUM":
            final_priority=2
        elif temp_priority.upper()=="HIGH":
            final_priority=3
        obj.is_priority =final_priority
        obj.save()
        return redirect('task_list')


def cancel_task(request, pk):
    task = get_object_or_404(DeliveryTask, pk=pk)
    task.status="cancelled"
    task.transition+="--cancelled"
    task.save()
    return redirect('task_list')



#views related to delivery person

def delivery_person_tasks(request):
    template_name = 'delivery/delivery.html'
    user_id = request.user.id
    allow_accept = True
    task_list = list(DeliveryTask.objects.all().filter(status="new", is_available=True))
    task_list = sorted(task_list, key= lambda x: (x.is_priority, x.creation_date), reverse=True)

    for i in task_list:
        if user_id not in [int(s) for s in i.is_declined_by.split(',')]:
            item = i
            break
        else:
            continue

    accepted_task_of_user = list(DeliveryTask.objects.all().filter(is_accepted_by=request.user.username))
    pending_task = list(DeliveryTask.objects.all().filter(is_accepted_by=request.user.username, status="accepted"))
    if len(pending_task) == 3:
        allow_accept = False
    return render(request,template_name,{'item':item, 'accepted_task_of_user':accepted_task_of_user, 'user': request.user,
                                         'allow_accept':allow_accept})


def accept_task(request, pk):
    task = get_object_or_404(DeliveryTask, pk=pk)
    task.status="accepted"
    task.transition+="--accepted"
    task.is_available=False
    task.is_accepted_by=request.user.username
    task.save()
    return redirect('delivery_person_tasks')


def complete_task(request, pk):
    task = get_object_or_404(DeliveryTask, pk=pk)
    task.status = "completed"
    task.transition+="--completed"
    task.save()
    return redirect('delivery_person_tasks')

def decline_task(request, pk):
    task = get_object_or_404(DeliveryTask, pk=pk)
    task.status = "new"
    task.transition+="--declined"
    task.is_available = True
    task.is_declined_by += "," + str(request.user.id)
    task.save()
    messages.success(request, str(request.user.username)+" declined task "+str(task.title))
    return redirect('delivery_person_tasks')












#common login logout views
class UserFormView(View):
    #form_class = UserForm
    template_name = 'delivery/login.html'

    def get(self, request):
        #form = self.form_class(None)
        return render(request, self.template_name)

    def post(self, request):
        #form = self.form_class(request.POST)

        #if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                if username[-1] == 'M':
                    login(request, user)
                    return redirect('task_list')
                elif username[-1] == 'D':
                    login(request, user)
                    return redirect('delivery_person_tasks')

        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    return redirect('login_user')





