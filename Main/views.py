from django.shortcuts import render, redirect
from .models import Ecommerce
from .forms import addproduct
from django.core.paginator import Paginator
import io
from rest_framework.parsers import JSONParser
from .serializers import EcommerceSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def ecommerce_api(request):
    #GET is used to retrive the Data.
    if request.method == 'GET':
        json_data = request.body  #request.body is used to when additional content can be sent to the user.
        stream = io.BytesIO(json_data) #it streams the JSON data
        pythondata = JSONParser().parse(stream) #it converts JSON parse data to Python Data
        id = pythondata.get('id',None)  #if we get an id of an specific data
        if id is not None:                    #<--------then this code will execute
            stu = Ecommerce.objects.get(id=id) 
            serializer = EcommerceSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Ecommerce.objects.all()          #<---------if not then, this code will execute.
        serializer = EcommerceSerializers(stu, many=True) # serializer converts complex data into pyton data
        json_data = JSONRenderer().render(serializer.data)  #JSONrendered converts python data into JSON
        return HttpResponse(json_data, content_type='application/json')

    # POST is used to submit the data send by the User
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = EcommerceSerializers(data=pythondata, partial=True) #we used Partial so that a user can store partial Info.
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'} #it will return a msg that your data is submitted.
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #PUT is used to update a data which is already present
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Ecommerce.objects.get(id=id)
        serializer = EcommerceSerializers(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #DELETE is used to delete a particular data from database.
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Ecommerce.objects.get(id=id)
        stu.delete()
        res = {'msg':"Data Deleted!!"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')




def Ecommercefun(request):
    #we will use POST method because it hold the data.
    if request.method == 'POST': 
        # request.POST for Data & request.Files for files(images).
        fm = addproduct(request.POST, request.FILES)
        #is_valid is used to validate the data stored in the Form.
        if fm.is_valid():
            fm.save()
            #we redirect user to the same page so that data can not be submitted again and again after refreshing.
            return redirect('/')
    else:
        fm = addproduct()
    #Pagination
    stu = Ecommerce.objects.all().order_by('id')
    paginate = Paginator(stu, 2)#we can adjust the number of data we want to show on display.
    page_number = request.GET.get('page')
    finalData = paginate.get_page(page_number)
    lastpage = finalData.paginator.num_pages #this logic is applied to get the lastpage.
    #we have used Dictionary Key Value Pair here so that data can be transfered to the template page
    #Also we have used list comperehension so that we can display Number of pages on Screen.
    return render(request, 'homepage.html', {'form': fm, 'stu': finalData,'totalPages':lastpage, 'totalpage':[n+1 for n in range(lastpage)]})


def delete_Product(request, id):
    if request.method == 'POST':
        a = Ecommerce.objects.get(pk=id) #we have used id as primary key ,it will get the id of that data which has to be deleted.
        a.delete()
        return redirect('/')#redirect user to home page after deleting the data.


def update_Product(request, id):
    if request.method == 'POST':
        a = Ecommerce.objects.get(pk=id)
        b = addproduct(request.POST, request.FILES, instance=a) #we have used instance so that it render the data into template page.
        if b.is_valid:
            b.save()
            return redirect('/')
    else:
        a = Ecommerce.objects.get(pk=id)
        b = addproduct(instance=a)
    return render(request, 'edit.html', {'form': b})
