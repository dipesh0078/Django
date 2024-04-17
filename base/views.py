from django.shortcuts import render
from .models import Room


'''rooms=[
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Design'},
    {'id':3, 'name':'Developers'},
]'''



# Create your views here.
def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,"base/home.html", context)

def room(request,pk):
   ''' room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i'''
   room=Room.objects.get(id=pk)
   context={'room':room}
   return render(request,'base/Room.html',context)

def test(request):
    return render(request, 'main.html' )