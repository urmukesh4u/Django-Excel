from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Myupload, Employee
from .resources import EmployeeResource
from .forms import EmployeeForm
from tablib import Dataset 
import os
# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts':allPosts}
    return render(request, 'home.html', context)

def addimage(request):
    allImages = Myupload.objects.all()
    image = {'allImages':allImages}
    return render(request, 'addimage.html', image)

def send_files(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfiles")
        for f in myfile:
            Myupload(f_name=name, myfiles=f).save()
        return HttpResponse("OK")
    
def addexcel(request):
    return render(request, 'addexcel.html')
   
def excel_upload(request):
    if request.method == 'POST':
        employee_resource = EmployeeResource()
        dataset = Dataset()
        name = request.POST.get("filename")
        new_employees = request.FILES['uploadexcel']
        
        if not new_employees.name.endswith('xlsx'):
            return HttpResponse("FILE FORMAT NOT VALID")
            
        imported_data = dataset.load(new_employees.read(),format='xlsx')
        for data in imported_data:
            value = Employee(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8], 
            )
            value.save()
    # return render(request,'home.html')
    return HttpResponse("FILE UPLOADED SUCCESSFULLY")
        
        
            
def addEmployee(request):    
    if request.method == "POST":
        empid = request.POST['empid']
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        dept = request.POST['dept']
        doj = request.POST['doj']
        dob = request.POST['dob'] 
        empphoto = request.FILES['empphoto']
        
        empdetails=Employee(empid=empid, name=name, contact=contact, email=email, dept=dept, doj=doj, dob=dob, empphoto=empphoto)
        empdetails.save()
        return redirect('/addemployee')    
    else:    
        emp_details = Employee.objects.all()
        context = {'emp_details':emp_details}
        return render(request, 'addemployee.html', context)

def viewEmployee(request, id):
    object=Employee.objects.get(pk=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(object.empphoto)>0:
                os.remove(object.empphoto.path)
            object.empphoto = request.FILES['empphoto']
    form=EmployeeForm(request.POST,instance=object)
    if form.is_valid():
        form.save()
        object=Employee.objects.all()
        return redirect('/addemployee')

    return render(request, 'viewemp.html', {'object':object})

# def delete(request,id):
#     object = Employee.objects.get(pk=id)
#     if request.method == "POST":
#         if object:
#             object.delete()
#             return redirect('/addemployee')

#         else:
#             return HttpResponse("invalid user id")
#     else:
#         return render(request, 'delete.html', {'object':object})


def delete(request, id):
    object = Employee.objects.get(id=id)
    object.delete()
    return redirect('/addemployee')

