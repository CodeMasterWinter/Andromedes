from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError


def index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            company = request.POST['company']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'Inquiry by {sender_first} {sender_last} from {company}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
    }

    return render(request, "andromedesweb/index.html", context)


def business_card(request):

    context = {

    }

    return render(request, 'andromedesweb/business-card.html', context)


def business_cards(request):

    context = {

    }

    return render(request, 'andromedesweb/business-cards.html', context)