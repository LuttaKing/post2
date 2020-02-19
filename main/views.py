from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    post={'PostString':Post.objects.all}
    
    return render(request, "main/home.html", context=post)

@csrf_exempt
def post_data(request):
    

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)

        if form.is_valid():
            # details=form.save()
            form.save()
            
    # if a GET (or any other method) we'll create a blank form
    # else:
        # form = PostForm()

    return render(request, 'main/form.html')
