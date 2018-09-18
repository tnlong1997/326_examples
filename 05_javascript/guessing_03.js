// Guessing Game 02

let randomNumber = Math.floor(Math.random() * 100) + 1;

let guesses = document.querySelector('.guesses');
let lastResult = document.querySelector('.lastResult');
let lowOrHi = document.querySelector('.lowOrHi');

let guessSubmit = document.querySelector('.guessSubmit');
let guessField = document.querySelector('.guessField');

let guessCount = 1;
let resetButton;

guessSubmit.addEventListener('click', checkGuess);

function checkGuess()
{
  let userGuess = Number(guessField.value);

  // Update the UI to show the previous guesses.
  if (guessCount === 1) {
    guesses.textContent = 'Previous guesses: ';
  }
  guesses.textContent += userGuess + ' ';

  // Evaluate the user's guess.
  if (userGuess === randomNumber)
  {
    lastResult.textContent = 'Congratulations! You got it right!';
    lastResult.style.backgroundColor = 'green';
    lowOrHi.textContent = '';
    setGameOver();
  }
  else if (guessCount === 10)
  {
    lastResult.textContent = '!!!GAME OVER!!!';
    setGameOver();
  }
  else
  {
    lastResult.textContent = 'Wrong!';
    lastResult.style.backgroundColor = 'red';
    if (userGuess < randomNumber)
    {
      lowOrHi.textContent = 'Last guess was too low!';
    }
    else if (userGuess > randomNumber)
    {
      lowOrHi.textContent = 'Last guess was too high!';
    }
  }

  guessCount++;

  // Reset the UI to prepare for next guess or Game Over.
  guessField.value = '';
  guessField.focus();
}

function setGameOver()
{
  guessField.disabled = true;
  guessSubmit.disabled = true;
  resetButton = document.createElement('button');
  resetButton.textContent = 'Start New Game';
  document.body.appendChild(resetButton);
  resetButton.addEventListener('click', resetGame);
}

