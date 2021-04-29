from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import QuestionForm
from .models import User,Questions,Answers

# Create your views here.
def index(request):
    return render(request, "covid/index.html")

def assess(request):
    return render(request, "covid/assess.html")

def info(request):
    return render(request,"covid/info.html")


def ask_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        try:
            new_question = form.save(commit=False)
            assert request.user.is_authenticated
            new_question.author = request.user
            new_question.save()
            return HttpResponseRedirect(reverse("index"))

        except ValueError:
            # Form was not valid, let's just return it back to the user so they can fix it
            pass

    else:
        form = QuestionForm()
    return render(request, "covid/ask-question.html", {
        "form": form
    })

def answer_ques(request, question_id):
    if request.method == "POST":
        assert request.user.is_authenticated
        try:
            question = Questions.objects.get(pk=question_id)
        except Questions.DoesNotExist:
            question = None
        answer_content = request.POST['answer']
        answer = Answers(question=question, ans=answer_content)
        answer.save()
    return HttpResponseRedirect(reverse("qna_page", args=(question_id,)))

def qna_page(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        question = None
    return render(request, "covid/qna.html", {
        'questions': Questions.objects.all,
        })
	

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "covid/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "covid/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "covid/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "covid/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "covid/register.html")