from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    all_projects = Project.objects.all()
    context = {"projects": all_projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    single_project = Project.objects.get(id=pk)
    tags = single_project.tags.all()
    context = {'project': single_project,'tags': tags}
    return render(request, 'single-project.html', context)


def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {"form": form}
    return render(request, 'add-project.html',context);


def update_project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {"form": form}
    return render(request, 'add-project.html',context);


def delete_project(request,pk):
    project =  Project.objects.get(id=pk)
    if request.method == 'POST':
        print('yoo')
        project.delete()
        return redirect('projects')
    context = {'project':project}
    return render(request,'confirm-delete.html',context)
