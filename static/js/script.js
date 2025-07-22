// --- Selecting all required elements from the DOM ---
const startBtn = document.querySelector(".start_btn button");
const infoBox = document.querySelector(".info_box");
const exitBtn = infoBox.querySelector(".buttons .quit");
const continueBtn = infoBox.querySelector(".buttons .restart");
const quizBox = document.querySelector(".quiz_box");
const resultBox = document.querySelector(".result_box");
const optionList = document.querySelector(".option_list");
const timeLine = document.querySelector("header .time_line");
const timeText = document.querySelector(".timer .time_left_txt");
const timeCount = document.querySelector(".timer .timer_sec");
const nextBtn = document.querySelector("footer .next_btn");
const bottomQuesCounter = document.querySelector("footer .total_que");
const restartQuizBtn = resultBox.querySelector(".buttons .restart");
const quitQuizBtn = resultBox.querySelector(".buttons .quit");

// --- Audio elements for feedback ---
const correctSound = document.getElementById("correctAudio");
const wrongSound = document.getElementById("wrongAudio");

// --- Quiz State Variables ---
let questions = []; // This will be populated by the API call
let timeValue = 15;
let queCount = 0;
let queNumb = 1;
let userScore = 0;
let counter;
let counterLine;

// --- Icon Tags for Correct/Incorrect Answers ---
const tickIconTag = '<div class="icon tick"><i class="fas fa-check"></i></div>';
const crossIconTag = '<div class="icon cross"><i class="fas fa-times"></i></div>';

// --- Global function to fetch questions from the server ---
window.fetchAndUpdateQuestions = (topic, start, end) => {
    continueBtn.disabled = true; // Disable button while fetching
    optionList.innerHTML = '<div class="option"><span>Loading...</span></div>';
    
    fetch(`/api/questions?topic=${topic}&start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            questions = data;
            continueBtn.disabled = false; // Re-enable button
            // The quiz will start when the user clicks 'Continue'
        })
        .catch(error => {
            console.error('Error fetching questions:', error);
            optionList.innerHTML = `<div class="option"><span>Failed to load questions.</span></div>`;
        });
};

// --- Event Listeners ---
startBtn.onclick = () => infoBox.classList.add("activeInfo");
exitBtn.onclick = () => infoBox.classList.remove("activeInfo");
quitQuizBtn.onclick = () => window.location.reload();

continueBtn.onclick = () => {
    infoBox.classList.remove("activeInfo");
    quizBox.classList.add("activeQuiz");
    startQuiz();
};

restartQuizBtn.onclick = () => {
    resultBox.classList.remove("activeResult");
    quizBox.classList.add("activeQuiz");
    startQuiz();
};

nextBtn.onclick = () => {
    if (queCount < questions.length - 1) {
        queCount++;
        queNumb++;
        showQuestions(queCount);
        queCounter(queNumb);
        resetTimer();
        nextBtn.classList.remove("show");
    } else {
        showResult();
    }
};

// --- Core Quiz Functions ---
function startQuiz() {
    resetQuizState();
    showQuestions(queCount);
    queCounter(queNumb);
    resetTimer();
}

function resetQuizState() {
    queCount = 0;
    queNumb = 1;
    userScore = 0;
}

function showQuestions(index) {
    if (!questions || questions.length === 0) {
        quizBox.classList.remove("activeQuiz");
        infoBox.classList.add("activeInfo");
        document.getElementById("output").textContent = "No questions loaded.";
        return;
    }
    const queText = document.querySelector(".que_text");
    let queTag = `<span>${questions[index].numb}. ${questions[index].question}</span>`;
    let optionTag = questions[index].options.map(option => `<div class="option"><span>${option}</span></div>`).join('');
    
    queText.innerHTML = queTag;
    optionList.innerHTML = optionTag;

    optionList.querySelectorAll(".option").forEach(option => {
        option.setAttribute("onclick", "optionSelected(this)");
    });
}

function optionSelected(answer) {
    clearInterval(counter);
    clearInterval(counterLine);
    const userAns = answer.textContent;
    const correctAns = questions[queCount].answer;

    if (userAns === correctAns) {
        userScore++;
        answer.classList.add("correct");
        answer.insertAdjacentHTML("beforeend", tickIconTag);
        correctSound.play().catch(e => console.log("Audio play failed"));
    } else {
        answer.classList.add("incorrect");
        answer.insertAdjacentHTML("beforeend", crossIconTag);
        wrongSound.play().catch(e => console.log("Audio play failed"));
        highlightCorrectAnswer();
    }
    disableAllOptions();
    nextBtn.classList.add("show");
}

function highlightCorrectAnswer() {
    const correctAns = questions[queCount].answer;
    for (let option of optionList.children) {
        if (option.textContent === correctAns) {
            option.classList.add("correct");
            option.insertAdjacentHTML("beforeend", tickIconTag);
        }
    }
}

function disableAllOptions() {
    for (let option of optionList.children) {
        option.classList.add("disabled");
    }
}

function showResult() {
    clearInterval(counter);
    clearInterval(counterLine);
    infoBox.classList.remove("activeInfo");
    quizBox.classList.remove("activeQuiz");
    resultBox.classList.add("activeResult");
    const scoreText = resultBox.querySelector(".score_text");
    let scoreTag = `<span>You got <p>${userScore}</p> out of <p>${questions.length}</p></span>`;
    scoreText.innerHTML = scoreTag;
}

function resetTimer() {
    clearInterval(counter);
    clearInterval(counterLine);
    startTimer(timeValue);
    startTimerLine();
    timeText.textContent = "Time Left";
}

function startTimer(time) {
    counter = setInterval(() => {
        timeCount.textContent = time < 10 ? `0${time}` : time;
        time--;
        if (time < 0) {
            clearInterval(counter);
            timeText.textContent = "Time Off";
            highlightCorrectAnswer();
            disableAllOptions();
            nextBtn.classList.add("show");
        }
    }, 1000);
}

function startTimerLine() {
    let time = 0;
    const timeStep = 100 / (timeValue * 1000 / 29);
    counterLine = setInterval(() => {
        time += timeStep;
        timeLine.style.width = time + "%";
        if (time > 100) {
            clearInterval(counterLine);
        }
    }, 29);
}

function queCounter(index) {
    const totalQueCounTag = `<span><p>${index}</p> of <p>${questions.length}</p> Questions</span>`;
    bottomQuesCounter.innerHTML = totalQueCounTag;
}
