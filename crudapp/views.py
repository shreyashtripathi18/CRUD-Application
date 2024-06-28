from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q


def index(request):
    students = Student.objects.all()
    query = ""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(
                name=name,
                email=email
                )
            messages.success(request, "Student Added Successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            
            update_student = Student.objects.get(id=id)
            update_student.name = name
            update_student.email = email
            update_student.save()

            messages.success(request, "Student Updated Successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()

            messages.success(request, "Student Deleted Successfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))



    context = {"students" : students, "query": query }
    return render(request, "index.html", context = context)
