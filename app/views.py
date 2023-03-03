# from django.shortcuts import rendera

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FormRequestForm
from .models import FormRequest

def form(request):
    if request.method == 'POST':
        form = FormRequestForm(request.POST)
        if form.is_valid():
            form_request = form.save()
            # send email to admin here
            return redirect('form_request_success')
    else:
        form = FormRequestForm()
    return render(request, 'forms.html', {'form': form})
