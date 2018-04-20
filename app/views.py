from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .form import ContactForm, HelloForm, UploadFileForm, CheckForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index_template(request):
    form    = ContactForm()
    contact = ContactForm()
    return render(request, 'index.html', {'form':form})

def hello_forms(request):
    form = HelloForm(request.GET or None)

    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'

    d = {
        'form':form,
        'message':message,
    }

    return render(request, 'forms.html', d)

@csrf_protect
def settingWindow(request):#, poll_id):

#    p = get_object_or_404(Poll, pk=poll_id)

    #form = ImageForm(request.GET or None)
    print("hello")

    raw_image_path = upload_file(request)
    if request.method == 'POST':
        checkbox =  CheckForm(request.POST)
        #if checkbox.is_valid():
            

    else:
        checkbox = CheckForm()

    print(checkbox['male'].value())
    #if form.is_varid():

    d = {
#            'poll':p
        'raw_image_path' : raw_image_path,
        'checkbox' : checkbox,
#        'message':message,
        #'raw':form.raw,
        #'cliped_image':clipped_image.raw,
        #'result_image':result_image.raw,
    }

    return render(request, 'forms.html', d)#, context_instance=RequestContext(request))

@csrf_protect
def handle_uploaded_file(f):
    print("hello")
    with open('raw_image.png', 'wb+') as destination:
        print("hello")
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_protect
def upload_file(request):
    print("hello")
    print(request.method)
    path = ''
    if request.method == 'POST':
        if 'upload' in request.FILES.keys():
            data = request.FILES['upload']
            path = default_storage.save('static/raw_image.png', ContentFile(data.read()))
        #with open("static/raw_image.png", "wb") as file:
            #tmp_file = os.path.join(MEDIA_ROOT, path)

            ##file.write(request.FILES['upload'])
            #book = form.save(commit=False)
            #if form.is_valid():
            #    book = form.save(commit=False)
            #    book.save()
            #file.write(request.content)
    return path
    #if request.method == 'POST':
    #    form = UploadFileForm(request.POST, request.FILES)
    #    if form.is_valid():
    #        book = form.save(commit=False)
    #        book.save()
    #        #print(request.FILES)
    #        #handle_uploaded_file(request.FILES['file'])
    #        #return HttpResponseRedirect('/success/url/')
    #else:
    #    form = UploadFileForm()

    #return form

