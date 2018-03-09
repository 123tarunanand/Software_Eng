from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL

@login_required()
def doc(request):
    if request.method == 'GET':
        p = USERMODEL.objects.get(name = request.user.username)
        if p.type != 'Patient':
            return HttpResponseRedirect('/home')
        sq = request.GET.get('docpr')
        if sq == None:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.filter(aname = sq)
        if not j:
            return HttpResponseRedirect('/home')
        sq = USERMODEL.objects.get(aname = sq)
        return render(request,'home/docprof.html',{'type':sq})

@login_required()
def main(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return render(request,'home/Gen.html')
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Public':
        return render(request,'home/Gen.html',{'name':k.aname})
    if k.type =='Patient':
        if request.method == 'GET':
            sq = request.GET.get('search_box')
            if sq !=None and sq.strip() :
                z = USERMODEL.objects.filter(name = sq,type = "Doctor")
                f = USERMODEL.objects.filter(aname = sq,type = "Doctor")
                g = USERMODEL.objects.filter(phno = sq, type = "Doctor")
                n = USERMODEL.objects.filter(qual = sq, type = "Doctor")
                p = USERMODEL.objects.filter(aname = sq, type = "Doctor")
                j = USERMODEL.objects.filter(field = sq, type = "Doctor")
                p = z|f|g|n|p|j
                return render(request,'home/rend.html',{'query':p,'name':sq})
        return render(request,'home/PAt.html',{'name':k.aname})
    if k.type == 'Doctor':
        return render(request,'home/Doc.html',{'name':k.aname})
