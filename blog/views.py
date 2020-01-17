from django.shortcuts import render

# Create your views here.

def post_list(request):
    print('I am here...')
    return render(request,'blog/post_list.html',{})
