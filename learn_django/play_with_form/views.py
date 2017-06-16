# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm, ContactForm


def name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it"s valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("thanks!")

    # if a GET (or any other method) we"ll create a blank form
    else:
        form = NameForm()

    return render(request, "forms/name.html", {"form": form})


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        contact_form = ContactForm(request.POST)
        # check whether it"s valid:
        if contact_form.is_valid():
            subject = contact_form.cleaned_data["subject"]
            message = contact_form.cleaned_data["message"]
            sender = contact_form.cleaned_data["sender"]
            cc_myself = contact_form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

            return HttpResponse("thanks")

    # if a GET (or any other method) we"ll create a blank form
    else:
        contact_form = ContactForm()

    return render(request, "forms/contact.html", {"form": contact_form})
