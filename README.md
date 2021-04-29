<h1>COVID-19(Final Project)</h1>

- My Final Project is a site including information on Covid.The user can take an assessment including 4 questions to check if the person has any chance of getting the virus.The site also includes a Q/A which displays the questions asked and the user can login to ask questions and answer the same.
- The web application utilize Django (including model) on the back-end and JavaScript on the front-end and is mobile-responsive
- The home page links to a page having all symptoms and causes and precautions for Covid-19.

Installation:
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
- Go to website address and register an account.

**Final projecct inlcludes an App**
- covid


**covid files**
- views.py
  - register function
    - Handles registering for the app
  - login_view function
    - Handles logging in the app.
  - logout_view function
    - Handles logging out the app.
  - qna_page function
    - when request is made it returns qna.html file displaying all questions and answers
  - answer_ques function:
    - as the request is made the  answer is saved in the list of answers of particular question
  - ask_question function:
    - if request made is POST then the question is added 
    - else form is displayed for asking the question
  - info function:
    - it displays the info.html file containing information about the covid-19
  - assess function:
    - it returns assess.html to take an assessment
  - index function:
    - it displays the index.html file
- urls.py - all application URLs
- models.py(contains three models used in this project):
  - User
  - Answers is for answering questions in qna
  - Questions is for asking questions in qna
- forms.py:
  - ModelForm for Questions
- Templates(contains all application templates):
  - layout.html
    - -base for all the templates
  - assess.html
    - -the assessment page
  - index.html
    - -the home page linking to complete information about the virus
  - info.html
    - -shows the information page
  - login.html
    - -shows the login page
  - register.html
    - -shows the register page
  - qna.html
    - -shows all the submitted questions and answers
- admin.py - includes some admin classes and re-registered User model.
- static(contains all the static content)
  - styles.css and styles.scss
    - -styling the page
  - assess.js(script that runs assess.html)
    - function startGame
      - This starts the assessment
    - function setNextQuestion
      - This resets the assessment for the next question
    - function showQuestion
      - Displays the question
    - function resetState 
      - Resets the assessment
    - function selectAnswer
      - To select and add to right answers if it indicates less danger from virus
    - function endGame
      - Displays if the user is prone to virus or is safe from it as a result
    - Const questions
      - Includes list of questions and options

<h1>Requirements</h1>
There was no additional requirements.The web application utilize Django (including model) on the back-end and JavaScript on the front-end.
