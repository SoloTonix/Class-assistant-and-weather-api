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
    note = Note.objects.all().order_by('-id')
    courses = Course.objects.all() # Retrieve Data from the Database
    context = {'courses':courses} # Pass retrieved data to the frontend

    return render(request, 'core/admin/index.html', context)
    

 # Frontend Page 


# Course  C.R.U.D.

def CourseDetail(request, pk):
    course = Course.objects.get(id=pk)
    if course:
        notes = Note.objects.filter(course=course)
    context = {'course':course, 'notes':notes}
    return render(request, 'core/note/notes.html', context)


def CreateCourse(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user
            var.save()

            request.session['course_id'] = var.id
            messages.success(request, 'Your course book haas been created succesfully')
            return redirect('Index')
        else:
            messages.warning(request, 'Sorry something went wrong')
            return redirect('Index')
    else:
        form = CreateCourseForm()
    context = {'form':form}
    return render(request, 'core/course/create_course.html', context)

def UpdateCourse(request, pk):
    course = Course.objects.filter(id=pk)
    if request.method == 'POST':
        form = CreateCourseForm(instance=course)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, 'Invalid Form')
    else:
        form = CreateCourseForm()
    context = {"form":form}
    return render(request, 'core/course/update_course.html', context)


# Course notes C.R.U.D.
def CreateNote(request):
    course = Course.objects.get(pk=request.session['course_id'])
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.course = course
            var.save()

            messages.info(request, 'Note created')
            return redirect('Index')
        else:
            messages.warning(request, 'Sorry something went wrong')
    else:
        form = CreateNoteForm()
    context = {'form':form}
    return render(request, 'core/note/create.html', context)

def UpdateNote(request, pk):
    note = Note.objects.get(id=pk)
    form = CreateNoteForm(request.POST or None, instance=note)
    context = {'form':form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Success....')
        return redirect('Index')
    return render(request, 'core/note/update.html', context)

def DetailNote(request, pk):
    note = Note.objects.get(id=pk)
    context = {'note':note}
    return render(request, 'core/note/detail.html', context)

def DeleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    messages.success(request, 'This note has been successfully deleted...')
    return redirect('Index')



'''
def WeatherApi(request):
    API_KEY = '1234'
    context = {'data':data, 'query':query}
    if request.method == 'POST':
        CITY = request.POST.get('city')
        url = BASE_URL + 'apiid=' + API_KEY + '&q=' + CITY
        response = requests.get(url).json()
        data = response['main']['temp']
        query = models.City(city, temp)
        query.save()
    return render(request, '', context)


'''




        





