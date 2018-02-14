# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime


def index(request):
    return render (request, 'index.html')

def post_word(request):
    new_word = request.POST['new_word']
    new_w = {
        'color': request.POST['color'],
        'content':'{} {}'.format(new_word, datetime.now().strftime('%Y-%m-%d // %H:%M')) 
    }
    new_w = request.session['new_wo']
    request.session.save()
    request.session['new_wo'] = new_w
    print "please work"
    return redirect('/')    

def process(request):
    
    return render(request, 'index.html')

