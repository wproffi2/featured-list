from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        msg = request.POST.get('textfield', None)
        
        if msg:
            resp = {'msg': msg}
            return render(request, 'index.html', resp)
    
    return render(request, 'index.html', {})

