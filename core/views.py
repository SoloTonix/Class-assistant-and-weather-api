from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from.models import *
from.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Index(request):
    courses = Course.objects.filter(author=request.user).order_by('-created')# Retrieve Data from the Database
    context = {'courses':courses} # Pass retrieved data to the frontend

    return render(request, 'core/admin/index.html', context)
    

 # Frontend Page 


# Course  C.R.U.D.
@login_required
def CourseDetail(request, pk):
    
    course = Course.objects.get(id=pk)
    if course.author == request.user:
        notes = Note.objects.filter(course=course)
        if len(notes) == 0:
            return redirect("CreateNote", pk)
    context = {'course':course, 'notes':notes}
    return render(request, 'core/note/notes.html', context)

@login_required
def CreateCourse(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user
            var.save()

            messages.success(request, 'Your course book haas been created succesfully')
            return redirect('CourseDetail', var.pk)
        else:
            messages.warning(request, 'Sorry something went wrong')
            return redirect('Index')
    else:
        form = CreateCourseForm()
    context = {'form':form}
    return render(request, 'core/course/create_course.html', context)

@login_required
def UpdateCourse(request, pk):
    course = Course.objects.get(pk=pk)
    form = CreateCourseForm(instance=course)
    if course.author == request.user:
        if request.method == 'POST':
            form = CreateCourseForm(request.POST or None, instance=course)
            if form.is_valid():
                form.save()
                return redirect('Index')
            else:
                messages.success(request, 'Invalid Form')
        else:
            form = CreateCourseForm()
    context = {"form":form}
    return render(request, 'core/course/update_course.html', context)

def DeleteCourse(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('Index')


# Course notes C.R.U.D.
@login_required
def CreateNote(request, pk):
    course = Course.objects.get(pk=pk, author=request.user)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.course = course
            var.save()

            messages.info(request, 'Note created')
            return redirect('CourseDetail', course.pk)
        else:
            messages.warning(request, 'Sorry something went wrong')
    else:
        form = CreateNoteForm()
    context = {'form':form, 'course':course}
    return render(request, 'core/note/create.html', context)

@login_required
def UpdateNote(request, pk):
    note = Note.objects.get(id=pk)
    form = CreateNoteForm(instance=note)

    if note.course.author == request.user:
        if request.method == 'POST':
            form = CreateNoteForm(request.POST or None, instance=note)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Success....')
                return redirect('DetailNote', note.pk)
    
    context = {'form':form}
    return render(request, 'core/note/update.html', context)

@login_required
def DetailNote(request, pk):
    note = Note.objects.get(id=pk)
    course = note.course
    if note.course.author == request.user:
        context = {'note':note, 'course':course}
        return render(request, 'core/note/detail.html', context)

@login_required
def DeleteNote(request, pk):
    note = Note.objects.get(id=pk)
    if note.course.author == request.user:
        note.delete()
        messages.success(request, 'This note has been successfully deleted...')
        return redirect('Index')








        





