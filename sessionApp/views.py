from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def session_count_views(request):
    count = request.session.get('counts',30)
    totalCount = int(count) + 1
    request.session['counts'] = totalCount
    exp_date = request.session.get_expiry_date
    details = {'count':totalCount , 'expiryDate':exp_date}
    return render(request , 'sessioncount.html' , context = details)
