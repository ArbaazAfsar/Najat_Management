from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the full message
            full_message = f"Message from {name} ({email}):\n\n{message}"

            try:
                # Send email to the admin
                send_mail(
                    subject,
                    full_message,
                    email,  # From user's email
                    ['arbaazbinafsar@gmail.com'],  # Admin's email
                    fail_silently=False,  # Set to True if you want to suppress errors
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')  # Redirect to prevent resubmission on refresh
            except Exception as e:
                # Log the error in production (optional)
                messages.error(request, f"Error: {str(e)}")  # Display error to user
        else:
            messages.error(request, 'Please correct the email below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})