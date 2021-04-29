
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("assess",views.assess,name="assess"),
    path("ask_question", views.ask_question, name="ask question"),
    path("qna_page/<int:question_id>", views.qna_page, name="qna_page"),
    path("answer_ques/<int:question_id>", views.answer_ques, name="answer question"),
    path("info",views.info, name="info")
    
]
