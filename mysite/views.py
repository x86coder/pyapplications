import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Job, Step

def index(req):

    template = loader.get_template("mysite/index.html")
    
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

    context = {"allRecordsSorted" : allRecordsSorted}
    return HttpResponse(template.render(context, req))
