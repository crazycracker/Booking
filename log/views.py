#!python
# log/views.py
import time
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserCreateForm
from .models import classroom, labs,requestTable
from django.core.serializers.json import DjangoJSONEncoder
import json

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def registration_form(request):
    if request.method == 'POST':
        # Create a RegistrationForm instance with the submitted data
        form = UserCreateForm(request.POST)

        # is_valid validates a form and returns True if it is valid and
        # False if it is invalid.
        if form.is_valid():
            form.save()
            return render(request, "success.html")

            # This means that the request is a GET request. So we need to
            # create an instance of the RegistrationForm class and render it in
            # the template
    else:
        form = UserCreateForm()

    return render(request, "registration_form.html",
                  {"form": form})


@login_required(login_url="login/")
def cc1(request, room_number):
    return render(request, "cc1.html", {"number": room_number})


@login_required(login_url="login/")
def display(request, block_name):
    classes = classroom.objects.filter(block=block_name)
    return render(request, "classrooms.html", {"rooms": classes})


@login_required(login_url="login/")
def eventlist(request):
    if request.is_ajax():
        start = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(request.GET['start']))))
        end = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(request.GET['end']))))
        entries = requestTable.objects.filter(date=start[0:10]).all()
        json_list = []
        for entry in entries:
            id = entry.id
            title = entry.description
            startDateTime= str(entry.date) + " " + str(entry.time)
            allDay = False
            print(startDateTime)
            json_entry = {'start': startDateTime, 'allDay': allDay, 'title': title,'overlap':False}
            json_list.append(json_entry)

        return HttpResponse(json.dumps(json_list), content_type='application/json')