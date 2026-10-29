from django.shortcuts import render, redirect
from .models import Poll
from .forms import PollForm


def home(request):

    if request.method == "POST":
        form = PollForm(request.POST)

        if form.is_valid():
            language = form.cleaned_data['language']

            language.votes += 1
            language.save()

            return redirect('home')

    else:
        form = PollForm()

    polls = Poll.objects.all()

    return render(request, 'poll/home.html', {
        'form': form,
        'polls': polls
    })