from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def render_static(request):
    return render(request, 'static.html')

def manage_media(request):
    if request.method == 'POST':
       print("post data" , request.POST)
       print("files" , request.FILES)
       file_obj = request.FILES['myfile']


       print("My file name is", file_obj.name)
       fs = FileSystemStorage()
       
       filename = fs.save(file_obj.name, file_obj)
       file_url = fs.url(filename)

       print("After save filename is", filename)
       print("My file url is", file_url)
    
    
    return render(request, 'media.html')    
    