from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
arr =  ['Python' , 'R' , 'Java' , 'Java Script', 'PHP' , 'C' , 'C++', 'Swift', 'Ruby', 'DOT NET', 'VB SCRIPT', 'Go', 'Prolog' , 'Matlab']
globalcnt = dict()

def VOTE_APP(request):
    mydictionary = {
        "arr" : arr
    }
    return render(request,'VOTE_index.html',context=mydictionary)

def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        # if already exist then increment the value
        globalcnt[q]=globalcnt[q]+1
    else:
        # first occurrence
        globalcnt[q]=1
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'VOTE_index.html',context=mydictionary)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'VOTE_index.html',context=mydictionary)