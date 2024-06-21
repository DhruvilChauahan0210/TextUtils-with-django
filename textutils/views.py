#i have created this file -Chauhan Dhruvil
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home</h1>")

def analyze(request):
    #get text
    djtext=request.GET.get('text','default')

    #check checkbox values
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    smallcaps = request.GET.get('smallcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')

    #if want to remove punctuations
    if removepunc=='on':
        punctuations=''':()-[]{};!'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                 analyzed=analyzed+char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    #if want to convert in uppercase
    elif fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Text Capitalized', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #if want to convert in lowercase
    elif smallcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Text lowerised', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #if want to remove new line
    elif newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char != '\n':
                analyzed=analyzed+char
        params = {'purpose': 'New line Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #if want to remove extra space
    elif extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]== ' ' and djtext[index+1]== ' ':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # if want to count number of characters
    elif charcount == 'on':
        char_count = len(djtext)
        params = {'purpose': 'Number of Characters', 'analyzed_text': char_count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("remove new line")
# def spaceremover(request):
#     return HttpResponse("remove space")
# def charcount(request):
#     return HttpResponse("remove space")