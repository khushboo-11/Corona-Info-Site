const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')
const submitButton =  document.getElementById('submit-btn')


let shuffledQuestions, currentQuestionIndex
let countRightAnswers = 0

function startGame() {
  startButton.innerText='Prev'
  submitButton.style.display='none'
  nextButton.style.display='none'
  shuffledQuestions = questions.sort(() => Math.random() - .5)
  currentQuestionIndex = 0
  questionContainerElement.style.display = 'block'
  setNextQuestion()
  countRightAnswers = 0;
}

function setNextQuestion() {
  resetState()
  showQuestion(shuffledQuestions[currentQuestionIndex])
}

function showQuestion(question) {
  questionElement.innerText = question.question
  submitButton.style.display = 'none'
  nextButton.style.display='block'
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.innerText = answer.text
    button.classList.add('btn')
    if (answer.correct) {
      button.dataset.correct = answer.correct
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })
}

function resetState() {
  clearStatusClass(document.body)
  nextButton.style.display = 'none'
  submitButton.style.display= 'none'
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild)
  }
}

function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
  Array.from(answerButtonsElement.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (selectedButton.dataset = correct) {
    countRightAnswers++;
 }
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextButton.style.display = 'block'
    submitButton.style.display = 'none'
    
  } else {
    submitButton.style.display = 'block'
    startButton.style.display = 'none'
    nextButton.style.display= 'none'
  }

}

function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

function endgame(){
  resetState()
  submitButton.style.display = 'none'
  nextButton.style.display = 'none'

  if (countRightAnswers == 4){
    questionElement.innerText = 'Your infection risk is low!'
  }
  else{
    questionElement.innerText = 'You are prone to the virus! Stay at home'
  }
}
const questions = [
  {
    question: 'Are you experiencing any of the following symptoms',
    answers: [
      {text:'Cough',correct:false},
      {text:'Fever',correct:false},
      {text:'Difficulty in breathing',correct:false},
      {text:'Loss of sense of smell and taste',correct:false},
      {text:'None of the above',correct:true}
    ]   
  },
  {
    question: 'Have you ever had any of the following?',
    answers: [
      {text:'Diabetes',correct:false},
      {text:'Hypertension',correct:false},
      {text:'Lung disease',correct:false},
      {text:'Heart disease',correct:false},
      {text:'kidney disorder',correct:false},
      {text:'None of the above',correct:true}
      ]   
  
  },
  {
    question: 'Have you travelled anywhere internationally in last 28-45 days?',
    answers: [
      {text:'Yes',correct:false},
      {text:'No',correct:true}
    ]
  },
  {
    question: 'Which of following apply to you?',
    answers: [
     {text:'I have recently interacted or lived with someone who has tested positive for COVID-19', correct:false},
     {text:'I am a healthcare worker and I examined a COVID-19 confirmed case without protectice gear',correct:true},
     {text:'None of the above',correct:true}
    ]
  }
]


document.addEventListener('DOMContentLoaded', function() {
  startButton.addEventListener('click', startGame)
  nextButton.addEventListener('click', () => {
    currentQuestionIndex++
    setNextQuestion()
    })
  submitButton.addEventListener('click',endgame)
});