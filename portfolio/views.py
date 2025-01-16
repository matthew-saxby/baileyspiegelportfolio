from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def about(request):
    return render(request, 'portfolio/about.html')  # Render the About page

def gallery(request):
    return render(request, 'portfolio/gallery.html')  # Render the Gallery page

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Email content
            subject = f"New Message from {first_name} {last_name}"
            full_message = f"""
            You have received a new message from your website contact form.

            Name: {first_name} {last_name}
            Email: {email}

            Message:
            {message}
            """

            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['matt.saxb@gmail.com'],
                    fail_silently=False,
                )
                success = True
            except Exception as e:
                success = False
                print(f"Error sending email: {e}")

            # Confirmation message
            return render(request, 'portfolio/contact.html', {
                'form': ContactForm(),
                'success': success
            })
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})
