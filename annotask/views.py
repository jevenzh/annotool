import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from django.contrib.auth.models import User
from annotask.models import *


# import data_tools to fetch tasks

DATA_UPDATE_INTERVAL = 8    # hours

# Create your views here.

def index(request):
    return render(request, 'annotation/index.html', context=None)


# @cache_page(60 * 30)
@vary_on_cookie
@login_required
def new(request):
    # task distribution goes here
    # mydata = get_new_task()
    
    # keep some information in session
    session = request.session

    # check if the session get expired
    

    cached_records = cache.get('record_list', None)

    # cache the fetched tasks list from camillo database
    last_syncup_time = cache.get('last_syncup_time', datetime.datetime.utcnow())
    time_since_last_syncup = (datetime.datetime.utcnow() - last_syncup_time).total_seconds() / 3600.0
    if not cached_records or time_since_last_syncup > DATA_UPDATE_INTERVAL:
        # TODO fetch records from camillo database and store/update them in cache
        # code here
        cache.add('last_syncup_time', datetime.datetime.utcnow())
        cache.add('record_list', [])
        
        # updating the annotation task pool
        for record in cache.get('record_list'):
            if not CaseReportFiles.objects.filter(rid = record['rid']).exists():
                CaseReportFiles.objects.create(rid=record['rid'], crf_path=record['crf_path'])

    current_user  = request.user

    return render(request, 'annotation/task.html', context={"taskdata": _dispatch_task(current_user, session)})


def _dispatch_task(user, session):
    
    # join CaseReportFiles with AnnotationTasks
    # sort by the status score for each group, group by the record id

    # create the annotation task, set the status level to 0.6
    # AnnotationTasks.objects.create(...)

    # glob all the CRF files out and prepare the task data

    default_annot = {
        "start_time": "10:30",
        "end_time": "10:35",
        "category": "pain_level",
        "value": "0",
    }

    vdata = {
        "name": "Annotation task page powered by Vue.js",
        "record_id": "$xxxx",
        "patient_info": {
            "name": "",
            "gender": "",
            "age": "",
            "height": "",
            "weight": "",
        },
        "num_annot": 1,
        "annotations": [default_annot],
        "crf_files": {
          "type": "image", # image or doc
          "images": [
            {
              "url":
                "/temp/vue_logo_1.jpg",
              "alt": "vue-1",
            },
            {
              "url":
                "/data/vue_logo_2.png",
              "alt": "vue-2",
            },
            {
              "url":
                "/data/django_log.jpg",
              "alt": "django",
            },
          ],
          "docs": [
            {
              "path": "/data/test.docx",
              "alt": ""
            },
            {
              "path": "/temp/giphy.gif",
              "alt": ""
            }
          ],
        },
      }
    
    return vdata


@vary_on_cookie
@login_required
def submit_form(request):

    session = request.session

    # here we check if the session has expired
    # update the task status if it has expired, otherwise we parse the submission

    # UserAnnotations.create(...)
    # UserPatientInfo.create(...)


    # set the status level to 1 to mark the task as completed

    return HttpResponse("Not implemented yet.")
