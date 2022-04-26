from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from snacks.models import Snack

def list_snacks(request):
    snacks = Snack.objects.all()
    return render(request, 'list_snacks.html', {'snacks' : snacks})


from snacks.forms import SnackForm

def create_snack(request):
    form = SnackForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_snacks')

    return render(request, 'snack_form.html', {'form': form})


def update_snack(request, id):
    snack = Snack.objects.get(id=id)
    form = SnackForm(request.POST or None, instance=snack)

    if form.is_valid():
        form.save()
        return redirect('list_snacks')

    return render(request, 'snack_form.html', {'form': form, 'snack': snack})


def delete_snack(request, id):
    snack = Snack.objects.get(id=id)

    if request.method == 'POST':
        snack.delete()
        return redirect('list_snacks')

    return render(request, 'snack_delete_confirm.html', {'snack': snack})
