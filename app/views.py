from django.shortcuts import render, redirect
from .models import Car
from .forms import UserTextForm

def static_view(request):
	return render(request,"app/static.html")


def database(request):
	cars = Car.objects.all()
	return render(request,"app/databaseList.html", {'cars': cars})

def user_text_input(request):
    if request.method == 'POST':
        form = UserTextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_text_input')  # Redirect to a success page or wherever needed
    else:
        form = UserTextForm()

    return render(request, 'app/user_text_input.html', {'form': form})