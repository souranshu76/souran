# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.

class dashboard(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        #form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': 'test3'})

    def post(self, request, *args, **kwargs):
        pass
        #form = self.form_class(request.POST)
       # if form.is_valid():
            # <process form cleaned data>
         #   return HttpResponseRedirect('/success/')

        #return render(request, self.template_name, {'form': form})

class notes(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    template_name = 'notes.html'

    def get(self, request, *args, **kwargs):
        #form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': 'test'})

    #def post(self, request, *args, **kwargs):
     #   form = self.form_class(request.POST)
      #  if form.is_valid():
       #     # <process form cleaned data>
        #    return HttpResponseRedirect('/success/')

        #return render(request, self.template_name, {'form': 'test1'})
    
    