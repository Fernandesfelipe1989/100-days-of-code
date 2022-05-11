
from quiz import quiz
from ui import QuizInterface

if __name__ == "__main__":
    run_game = True
    QuizInterface()
    # while run_game:
    #     run_game = quiz.still_has_questions()

    print(f"Your final score is {quiz.final_score():.1f}%")
