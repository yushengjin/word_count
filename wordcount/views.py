from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html',{'hithere':'THis is me'})

def eggs(request):
    return HttpResponse('eggs r good')

def count(request):
    fulltext = request.GET['fulltext']

    print(fulltext)

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist), 'worddictionary1':sortedwords})

def good(request):
    return render(request, 'good.html')
