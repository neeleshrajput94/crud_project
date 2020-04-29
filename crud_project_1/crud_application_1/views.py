from django.shortcuts import render,redirect
from crud_application_1.forms import Student_form
from crud_application_1.models import Student

# Create your views here.

def welcome_page(request):
    return render(request, 'welcome.html')

def std(request):
    if request.method == "POST":
        form = Student_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = Student_form()
    return render(request, "index.html", {'form':form})

def show(request):
    students = Student.objects.all()
    return render(request, "show.html", {'students':students})

def edit(request, id):
    students = Student.objects.get(id=id)
    return render(request, "edit.html", {'student':students})

def update(request, id):
    students = Student.objects.get(id=id)
    form = Student_form(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {'students':students})

def delete(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("/show")
