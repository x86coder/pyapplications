import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Job, Step

def index(req):

    myjobs = Job.objects.all()
    allRecords = []
    discardedRecords = []

    for j in myjobs:
        record = []
        record.append(j.role_text)
        record.append(j.company_text)

        recordEvents = []
        most_recent_event_date = None
        for s in j.step_set.all():
            singleEvent = []
            dbdate = timezone.make_naive(s.date, timezone.get_current_timezone())
            singleEvent.append(s.name_text)
            singleEvent.append(dbdate)
            
            if most_recent_event_date == None:
                most_recent_event_date = dbdate
            else:
                if dbdate > most_recent_event_date:
                    most_recent_event_date = dbdate
            recordEvents.append(singleEvent)

        record.append(most_recent_event_date)
        record.append(sorted(recordEvents, key=lambda y:y[1], reverse=True))
        if j.discarded == True:
            discardedRecords.append(record)
        else:
            #if most_recent_event_date != None:
            allRecords.append(record)

    allRecordsSorted = sorted(allRecords, key=lambda x: x[2], reverse=True)
    discardedRecordsSorted = sorted(discardedRecords, key=lambda x: x[2], reverse=True)

    mytext = '<!DOCTYPE HTML><!-- <meta>Python application for managing job applications by x86coder</meta> --><HEAD><title>pyApplications</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script></HEAD>';
    mytext += '<BODY><div class="container-fluid"><H1> pyapplications </H1><HR><div class="card-columns">'

    #mytext += str(allRecordsSorted)
    #mytext += '<br><br>' + str(discardedRecordsSorted)

    for r in allRecordsSorted:
        
        mytext += '<div class="card border-dark" style="margin: 0.5em; width: 18rem; display: inline-block;">'
        mytext += '<div class="card-header">📁' + r[1] + '</div><div class="card-body"><p><b>Role: </b>' + r[0] + '</p>'
        mytext += 'events:<ul>'
        for e in r[3]:
            mytext += "<li>" + e[0] + " @ " + str(e[1]) +"</li>"
        mytext += "</ul></div></div>"

    mytext += '</div></div><div class="container-fluid"><H1> pyapplications (discarded)</H1><HR><div class="card-columns">'

    for d in discardedRecordsSorted:
        
        mytext += '<div class="card border-secondary" style="margin: 0.5em; width: 18rem; display: inline-block;">'
        mytext += '<div class="card-header">📌' + d[1] + '</div><div class="card-body"><p><b>Role: </b>' + d[0] + '</p>'
        mytext += 'events:<ul>'
        for e in d[3]:
            mytext += "<li>" + e[0] + " @ " + str(e[1]) +"</li>"
        mytext += "</ul></div></div>"

    mytext += "</div></div></body></HTML>"

    return HttpResponse(mytext)
