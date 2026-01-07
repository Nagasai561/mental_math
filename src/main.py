import audio
import qa
import time
from rich.console import Console
from rich.prompt import Prompt

console = Console()

total_time_sum = 0
total_questions = 0
correct_answers = 0

try:
    while True:
        question, answer = qa.generate_qa()
        audio.speak(question)

        start_time = time.time()
        user_answer = Prompt.ask("[cyan]Your answer")
        end_time = time.time()

        elapsed_time = end_time - start_time
        total_time_sum += elapsed_time
        total_questions += 1

        try:
            if int(user_answer) == answer:
                correct_answers += 1
                console.print("[green]Correct!")
            else:
                console.print(f"[red ]Incorrect. The correct answer is {answer}.")
        except ValueError:
            console.print("[magenta ]Invalid input")

except KeyboardInterrupt:
    # Exit the program on Ctrl+C
    # Print summary statistics
    console.print("[yellow]Exiting the program.")
    console.print(f"[yellow]Correct answers: {correct_answers}/{total_questions}")
    if total_questions > 0:
        console.print(
            f"[yellow]Average Time per Question: {total_time_sum / total_questions:.2f} seconds"
        )
