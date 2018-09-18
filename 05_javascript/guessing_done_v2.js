// Completed Guessing Game - Version 2.0
//  This version of the game demonstrates how to better organize a
//  JavaScript application. Rather than create global variables that
//  can accidentally (or maliciously) be tampered with we rely on two
//  important techniques: objects and anonymous function.
//
//  We also add some debugging output to show how you can use some
//  easy techniques to verify what we assume.
//

// This is equivalent to the "main" function of a traditional
// programming language. This is *very* important, otherwise, we will
// not have an entry point into the program and nothing will happen.
window.addEventListener('load', init);

// Returns a random number between 1 and 100.
function getRandomNumber()
{
  return Math.floor(Math.random() * 100) + 1;;
}

// Initializes the game UI and state.
function init()
{
  console.log('initializing Guessing Game');
  
  let UI = {
    guesses : document.querySelector('.guesses'),
    lastResult : document.querySelector('.lastResult'),
    lowOrHi : document.querySelector('.lowOrHi'),
    guessSubmit : document.querySelector('.guessSubmit'),
    guessField : document.querySelector('.guessField'),
    resultParas : document.querySelectorAll('.resultParas p')
  };

  let gameState = {
    randomNumber : getRandomNumber(),
    guessCount : 1
  };

  // We create an event listener that calls an "anonymous function"
  // when the "submit guess" button is "clicked".
  UI.guessSubmit.addEventListener('click', () => {
    console.log('Submit guess button was clicked');

    // We pass in the UI components and game state each time the
    // submit button is clicked. It is important to note that because
    // we create the UI and gameState objects inside the init function
    // they continue to live in this anonymous function.
    checkGuess(UI, gameState);
  });
}

function checkGuess(UI, gameState)
{
  let userGuess = Number(UI.guessField.value);

  // Update the UI to show the previous guesses.
  if (gameState.guessCount === 1) {
    UI.guesses.textContent = 'Previous guesses: ';
  }
  UI.guesses.textContent += userGuess + ' ';

  // Evaluate the user's guess.
  if (userGuess === gameState.randomNumber)
  {
    UI.lastResult.textContent = 'Congratulations! You got it right!';
    UI.lastResult.style.backgroundColor = 'green';
    UI.lowOrHi.textContent = '';
    setGameOver(UI, gameState);
  }
  else if (gameState.guessCount === 10)
  {
    UI.lastResult.textContent = '!!!GAME OVER!!!';
    setGameOver(UI, gameState);
  }
  else
  {
    UI.lastResult.textContent = 'Wrong!';
    UI.lastResult.style.backgroundColor = 'red';
    if (userGuess < gameState.randomNumber)
    {
      UI.lowOrHi.textContent = 'Last guess was too low!';
    }
    else if (userGuess > gameState.randomNumber)
    {
      UI.lowOrHi.textContent = 'Last guess was too high!';
    }
  }

  gameState.guessCount++;

  // Reset the UI to prepare for next guess or Game Over.
  UI.guessField.value = '';
  UI.guessField.focus();
}

function setGameOver(UI, gameState)
{
  UI.guessField.disabled = true;
  UI.guessSubmit.disabled = true;
  UI.resetButton = document.createElement('button');
  UI.resetButton.className = 'btn btn-primary';
  UI.resetButton.textContent = 'Start New Game';
  document.body.appendChild(UI.resetButton);

  UI.resetButton.addEventListener('click', () => {
    console.log('Start New Game buttom was clicked');
    resetGame(UI, gameState);
  });
}

function resetGame(UI, gameState)
{
  gameState.guessCount = 1;

  let resultParas = UI.resultParas;
  for (let i = 0; i < resultParas.length; i++)
  {
    resultParas[i].textContent = '';
  }

  UI.resetButton.parentNode.removeChild(UI.resetButton);

  UI.guessField.disabled = false;
  UI.guessSubmit.disabled = false;
  UI.guessField.value = '';
  UI.guessField.focus();

  UI.lastResult.style.backgroundColor = 'white';

  gameState.randomNumber = getRandomNumber();

  console.log('Guessing Game was reset');
}
