from django.http import HttpResponse
from django.shortcuts import redirect, render

from pages.models import Feedback

def home(request):
    return HttpResponse("You are at home page")

def about(request):
    return HttpResponse("You are at about page")

def contact(request):
    return HttpResponse("You are at contact page")


def feedback(request):
    if request.method == "POST":
        rating_raw = request.POST.get("rating", "0")
        try:
            rating_value = int(rating_raw)
        except ValueError:
            rating_value = 0

        Feedback.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            rating=rating_value,
            message=request.POST.get("message", "").strip(),
        )
        return redirect("feedback")

    feedback_items = Feedback.objects.all()
    return render(request, "feedback.html", {"feedback_items": feedback_items})


