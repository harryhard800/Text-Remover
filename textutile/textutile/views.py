from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def anlayze(request):
    djtext = (request.POST.get('text', 'default'))
    re = (request.POST.get('Removed', 'off'))
    upper = request.POST.get('upper', 'off')
    new_line_remover = request.POST.get("NEW",'off')
    punctuations = '''!-[]{};:()'"\,<>/?#$%^&*_~'''

    if upper=='on':
        a = ''
        for char in djtext:
            a += char.upper()
        djtext = a
    if re == 'on':
        a = ''
        for char in djtext:
            if char not in punctuations:
                a += char
        djtext = a
    if new_line_remover == "on":
        a = ""
        for char in djtext:
            if char != '\n' and char !='\r':
                a += char
        djtext = a
    params = {'purpose': 'Text after modification is', 'analyze_text': djtext}
    if new_line_remover != "on" and upper != 'on' and re!= 'on':
        return HttpResponse('ERROR! please Select any one option and try again')
    return render(request,'analyze.html',params)
print()