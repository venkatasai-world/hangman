🎮 Vang Man Game

Vang Man is a simple word guessing game (like Hangman) built using Python (Flask) for the backend and HTML/CSS for the frontend. The goal is to guess a randomly selected animal name by entering letters. You win if you guess the word before chances run out.

How to Run:

1. Clone the repository:
   git clone https://github.com/your-username/vangman.git
   cd vangman

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app locally:
   python app.py

4. Or run with Gunicorn (for production):
   gunicorn app:app

Features:

- Random animal word selection
- Shows blank underscores for hidden letters
- Reveals correct letters after guess
- Tracks guessed letters and chances left
- Win/Lose message with option to play again
- Responsive and clean interface

Files:

- app.py - Backend code using Flask
- templates/index.html - Frontend in one HTML+CSS file
- requirements.txt - List of required Python packages

Enjoy playing the Vang Man Game!
