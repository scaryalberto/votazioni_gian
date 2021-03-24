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
from .models import CandidatiUomo, CandidatiDonna, Votes
from .forms import CandidatiUomoVotes
from datetime import datetime

'''
@login_required
def voti(request):
    posts={}
    return render(request, 'votazioni/voti.html', {'posts': posts})
'''

def votazioni(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts={}
    return render(request, 'votazioni/home.html', {'posts': posts})


import pytz
from datetime import datetime, timezone


@login_required
def voti(request):
    ha_votato = Votes.objects.get(user_id=request.user.id)

    if request.method=="POST" and ha_votato.ha_votato == False:#dopo che clicchi vota parte la post

        #ha_votato.filter(user_id=3).values()[0]['ha_votato'] == True

        try:
            id_candidato = int(request._post['choice'])
        except:
            candidati = CandidatiUomo.objects.all()
            return render(request, 'votazioni/voti.html', {'candidati': candidati})

        ha_votato.ha_votato=True
        ha_votato.save()
        candidati=CandidatiUomo.objects.get(id=id_candidato)
        #candidati= CandidatiUomo.objects.all()
        candidati.votes +=1
        candidati.save()
        tz = pytz.timezone('Europe/Rome')


        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()  # local time

        orario_voto = 'Hai votato ' + candidati.nome_e_cognome.upper() + ' in data ' + utc_dt.strftime("%d/%m/%Y %H:%M:%S")



    else:
        orario_voto=''
        # print(request.POST['choice'])
        candidati= CandidatiUomo.objects.all()

    candidati = CandidatiUomo.objects.all()
    return render(request, 'votazioni/voti.html', {'candidati': candidati, 'orario_voto':orario_voto})
