from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import NominationPage, Nominee
from datetime import datetime


def getNominees(request, slug):
    retrievedObj = NominationPage.objects.filter(slug = slug)
    if retrievedObj[0].date <= datetime.now():
        print("time to vote")
        nominees = Nominee.objects.filter(nomination_page__slug = slug).all().order_by('position')
        context = {
            'election': retrievedObj[0],
            'election_date': retrievedObj[0].date.strftime("%Y-%m-%d"),
            'tab': 'elections',
            'authenticated' : request.user.is_authenticated,
            'nominees' : nominees
        }
        return render(request, 'elections/nominee_list.html', context)
    else:
        print("cant vote yet")
        context = {
            'tab': 'elections',
            'nominees' : 'none',
            'authenticated' : request.user.is_authenticated,
        }
        return render(request, 'elections/nominee_list.html', context)
