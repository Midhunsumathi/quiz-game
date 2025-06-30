Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> <!DOCTYPE html>
... <html>
... <head>
...   <meta charset="utf-8">
...   <title>Quiz App</title>
...   <style>
...     body { font-family: sans-serif; max-width: 600px; margin: auto; }
...     .option { display: block; margin: 8px 0; padding: 8px; cursor: pointer; }
...     .restart-btn { display: none; margin-top: 20px; }
...   </style>
... </head>
... <body>
...   <h2 class="question"></h2>
...   <div id="time">30</div>
...   <div class="options"></div>
...   <div class="result" style="display:none;">
...     <h3>Your score: <span id="score">0</span></h3>
...   </div>
...   <button class="restart-btn">Restart Quiz</button>
... 
...   <script>
...     const quizData = [
...       { question: "Capital of France?", options: ["Berlin","Madrid","Paris","Lisbon"], answer: "Paris" },
...       { question: "Web dev language?", options: ["Python","HTML","Java","C++"], answer: "HTML" },
...       { question: "Writer of Hamlet?", options: ["Dickens","Shakespeare","Twain","Austen"], answer: "William Shakespeare" },
...       { question: "Largest planet?", options: ["Earth","Mars","Jupiter","Saturn"], answer: "Jupiter" },
...       { question: "Land of the Rising Sun?", options: ["China","Japan","S.Korea","India"], answer: "Japan" }
...     ];
... 
...     let currentQuestion = 0, score = 0, timeLeft = 30, timerInterval;
...     const timerEl = document.getElementById('time');
...     const questionEl = document.querySelector('.question');
...     const optionsEl = document.querySelector('.options');
...     const resultEl = document.querySelector('.result');
...     const scoreEl = document.getElementById('score');
...     const restartBtn = document.querySelector('.restart-btn');
... 
...     function loadQuestion() {
...       if (currentQuestion >= quizData.length) return endQuiz();
... 
...       clearInterval(timerInterval);
...       timeLeft = 30;
...       timerEl.textContent = timeLeft;
...       startTimer();
... 
      const q = quizData[currentQuestion];
      questionEl.textContent = q.question;
      optionsEl.innerHTML = '';
      q.options.forEach(opt => {
        const btn = document.createElement('button');
        btn.classList.add('option');
        btn.textContent = opt;
        btn.onclick = () => checkAnswer(opt);
        optionsEl.appendChild(btn);
      });
    }

    function checkAnswer(opt) {
      if (opt === quizData[currentQuestion].answer) score++;
      currentQuestion++;
      loadQuestion();
    }

    function startTimer() {
      timerInterval = setInterval(() => {
        timeLeft--;
        timerEl.textContent = timeLeft;
        if (timeLeft <= 0) {
          clearInterval(timerInterval);
          endQuiz();
        }
      }, 1000);
    }

    function endQuiz() {
      clearInterval(timerInterval);
      questionEl.style.display = 'none';
      optionsEl.style.display = 'none';
      resultEl.style.display = 'block';
      scoreEl.textContent = score;
      restartBtn.style.display = 'block';
    }

    restartBtn.onclick = () => {
      currentQuestion = score = 0;
      questionEl.style.display = '';
      optionsEl.style.display = '';
      resultEl.style.display = 'none';
      restartBtn.style.display = 'none';
      loadQuestion();
    };

    loadQuestion();
  </script>
</body>
