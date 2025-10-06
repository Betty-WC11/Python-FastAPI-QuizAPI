# The Content Creator - holds the sample data for your quiz
# You define a Quiz object here with real questions and answers.
# Later, you can replace this with a database or external API.


from app.models import Quiz, Question

sample_quiz = Quiz(
    id=1,
    title="General Knowledge",
    questions=[
        Question(
            id=1,
            question="What is the capital of France?",
            options=["Berlin", "Madrid", "Paris", "Rome"],
            answer_index=2,
        ),
        Question(
            id=2,
            question="Which planet is known as the Red Planet?",
            options=["Earth", "Mars", "Jupiter", "Venus"],
            answer_index=1,
        ),
    ],
)

