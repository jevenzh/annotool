from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from annotask.models import CaseReportFiles, AnnotationTasks

# import data_tools to fetch tasks

# Create your views here.


def index(request):
    return render(request, 'annotation/index.html', context=None)


@login_required
def new(request):
    # TODO task distribution goes here
    # mydata = get_new_task()
    return render(request, 'annotation/task.html', context={"taskdata": dispatch_task()})


def dispatch_task():
    default_annot = {
            "start_time": "10:30",
            "end_time": "10:35",
            "category": "pain_level",
            "value": "0",
        }
    vdata = {
        "name": "Annotation task page powered by Vue.js",
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
