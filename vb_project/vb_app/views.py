from django.shortcuts import render, redirect
from .models import Worker
from .forms import WorkerForm


def worker_list(request):
    template = 'worker_functionality/worker_list.html'
    context = {
        'worker_list': Worker.objects.all()
    }
    return render(request, template, context)


def worker_form(request, id=0):
    template = 'worker_functionality/worker_form.html'
    if request.method == 'GET':
        if id == 0:
            """
            If id is 0, then a new instance of the WorkerForm() form is created, which will be 
            used to create a new entry.
            """
            form = WorkerForm()
        else:
            """
            If id is not equal to 0, then an existing Worker entry with the given id is found, 
            and this object is used to initialize the WorkerForm(instance=worker) form. Here, 
            the form will be pre-filled with the data of the existing record for editing.
            """
            worker = Worker.objects.get(pk=id)
            form = WorkerForm(instance=worker)
        return render(request, template, {'form': form})
    # If the request method is not GET (else), it means that a form was submitted.
    else:
        """
        If id is 0, it means the user is trying to create a new post. A WorkerForm(request.POST) 
        is instantiated using the data submitted by the user via a POST request.
        """
        if id == 0:
            form = WorkerForm(request.POST)
        else:
            """
            If id is not equal to 0, it means that the user is trying to update an existing record. 
            The corresponding Worker object is found, and the form is initialized with the entry's data 
            using WorkerForm(request.POST, instance=worker).
            """
            worker = Worker.objects.get(pk=id)
            form = WorkerForm(request.POST, instance=worker)

        if form.is_valid():
            form.save()
        return redirect('worker_list')


def worker_delete(request, id):
    worker = Worker.objects.get(pk=id)
    worker.delete()
    return redirect('worker_list')




