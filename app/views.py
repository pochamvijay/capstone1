from django.shortcuts import render, redirect
from app.models import Student


# HOME PAGE

def index(request):

    data = Student.objects.all()

    context = {
        'data': data
    }

    return render(request, 'app/index.html', context)


# INSERT DATA

def insertdata(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        Student.objects.create(

            name=name,
            email=email,
            age=age,
            gender=gender
        )

        return redirect('/')

    return redirect('/')


# DELETE

def deleteData(request, id):

    data = Student.objects.get(id=id)

    data.delete()

    return redirect('/')


# EDIT PAGE

def editData(request, id):

    data = Student.objects.get(id=id)

    context = {
        'd': data
    }

    return render(request, 'app/edit.html', context)


# UPDATE

def updateData(request, id):

    data = Student.objects.get(id=id)

    data.name = request.POST.get('name')
    data.email = request.POST.get('email')
    data.age = request.POST.get('age')
    data.gender = request.POST.get('gender')

    data.save()

    return redirect('/')