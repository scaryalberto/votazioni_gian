from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Crea le tue views qui.


#def post_list(request):
#    return render(request, '/home/alberto/PycharmProjects/my_blog/mysite/templates/blog/post_list.html', {})

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from django.utils import timezone
#from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def voti(request):
    posts={}
    return render(request, 'votazioni/voti.html', {'posts': posts})


def votazioni(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts={}
    return render(request, 'votazioni/home.html', {'posts': posts})
