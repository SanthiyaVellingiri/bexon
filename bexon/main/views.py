from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')
def about(request):
  return render(request,'about.html')
def contact(request):
  return render(request,'contact.html')
def career(request):
  return render(request,'career.html')
def services(request):
  return render(request,'services.html')

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_form_submit(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        location = request.POST.get("Location")
        phone = request.POST.get("Phone")
        message = request.POST.get("Message")

        try:
            subject = f"New Contact Form Submission from {name}"
            body = f"""
              You have received a new message from your website contact form.

              Name: {name}
              Email: {email}
              Location: {location}
              Phone: {phone}

              Message:
              {message}
              """

            
            from_email = f"{name} <no-reply@techssoftinnovations.com>"

            mail = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=["tech@techssoftinnovations.com"],  # your mailbox
                reply_to=[email]  # if you click Reply, goes to the user
            )
            mail.send(fail_silently=False)

            return JsonResponse({"status": "success", "message": "Message sent successfully!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def career_form_submit(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        location = request.POST.get("Location")
        phone = request.POST.get("Phone")
        position = request.POST.get("Position")
        message = request.POST.get("Message")
        resume = request.FILES.get("Resume")

        try:
            subject = f"New Career Form Submission from {name}"
            body = f"""
            You have a new candidate submission:

            Name: {name}
            Email: {email}
            Location: {location}
            Phone: {phone}
            Position Applied: {position}
            Message:
            {message}
            """

            mail = EmailMessage(
                subject=subject,
                body=body,
                from_email=f"{name} <no-reply@techssoftinnovations.com>",
                to=["tech@techssoftinnovations.com"],
                reply_to=[email]
            )

            # Attach resume if uploaded
            if resume:
                mail.attach(resume.name, resume.read(), resume.content_type)

            mail.send(fail_silently=False)

            return JsonResponse({"status": "success", "message": "Your application has been sent!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})
