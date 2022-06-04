from django.shortcuts import render
from django.http import request
from . import translate

# Create your views here.


def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = translate.transalte(original_text)
        return render(request, 'translate.html', {'output_text': output, 'original_text': original_text})
    else:
        return render(request, 'translate.html')
