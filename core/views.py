from django.shortcuts import render,redirect
from .models import Finger
import tempfile
import os

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age =  request.POST.get('age')
        phone = request.POST.get('phone')
        address =  request.POST.get('add')
        image =  request.FILES.get('photo')
        finger = Finger.objects.create(name=name,age=age,adress=address,image=image,phone=phone)
        finger.save()
    return render(request,'pages/index.html')

def scan(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        temp_file = tempfile.NamedTemporaryFile(delete=False)

        with open(temp_file.name, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # uploaded image path = the path of the uploaded image
        uploaded_image_path = temp_file.name
        
        # when you get the finger instance just uncomment this line of code to use it in view_results view
        # request.session['finger] = finger_instance

    return render(request,'pages/scan.html')

def view_results(request):
    finger = request.session.get('finger')
    context = {'finger':finger}
    return render(request,'pages/viewdata.html',context)

