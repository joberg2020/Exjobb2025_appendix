import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch, AsyncMock

from progression.core.analysis import analyse
from progression.schemas import (
    QuizResultRead, Score, QuizStatus, QuizMode, QuestionType,
    Level,
)
from test_x import make_response_with_json


# Fixtures
F_JAWS = [
    (4, 10, 5), (3, 15, 4), (2, 20, 3), (1, 25, 2), (0, 30, 1)
]
F_CLIMB = [
    (4, 10, 1), (3, 15, 1), (2, 20, 1), (1, 25, 1), (0, 30, 1)
]
F_TAKE_OFF = [
    (4, 5, 5), (3, 10, 5), (2, 15, 5), (1, 20, 5), (0, 25, 5)
]
F_SNOW_PLOW = [
    (4, 20, 1), (3, 15, 2), (2, 10, 3), (1, 5, 4), (0, 3, 5)
]
F_AIM = [
    (4, 30, 0), (3, 31, 0), (2, 30, 0), (1, 32, 0), (0, 31, 0)
]
F_AIM_CLOSE = [
    (4, 29, 0), (3, 29, 1), (2, 29, 0), (1, 29, 0), (0, 31, 0)
] # Not reaching the target two days in a row
F_MID_LEVEL = [
    (4, 5, 10), (3, 5, 11), (2, 5, 10), (1, 5, 11), (0, 5, 11)
]
F_SURFACE = [
    (4, 10, 1), (3, 10, 2), (2, 10, 3), (1, 10, 4), (0, 10, 5)
]
F_DOWNHILL = [
    (4, 20, 10), (3, 15, 8), (2, 10, 6), (1, 6, 4), (0, 4, 2)
]
F_LANDING = [
    (4, 20, 5), (3, 15, 5), (2, 10, 5), (1, 5, 5), (0, 3, 5)
]
F_DIVE = [
    (4, 9, 8), (3, 9, 6), (2, 9, 4), (1, 9, 2), (0, 9, 1)
]
F_UPHILL = [
    (4, 5, 2), (3, 6, 3), (2, 7, 4), (1, 8, 5), (0, 9, 6)
]
F_CROSSOVER_JAWS = [
    (4, 5, 15), (3, 9, 13), (2, 13, 10), (1, 17, 7), (0, 25, 3)
]
F_DATA_TOO_THIN = [(2, 10, 3), (1, 5, 4), (0, 3, 5)
]

F_MULTIPLE_VALUES_PER_DAY = [
    (4, 20, 5), (4, 15, 6), (4, 25, 4), (4, 20, 1),
    (3, 15, 2),
    (2, 10, 3), (2, 10, 3),
    (1, 5, 4), (1, 3, 5), (1, 10, 3),
    (0, 5, 4), (0, 3, 5),
]

@pytest.mark.asyncio
@pytest.mark.parametrize("name, fixture_data, expected_picture, expected_action, expected_status", [
    ("F-JAWS", F_JAWS, "JAWS", "KEEP_GOING", "OK_PROGRESS"),
    ("F-CLIMB", F_CLIMB, "CLIMB", "KEEP_GOING", "OK_PROGRESS"),
    ("F-TAKE_OFF", F_TAKE_OFF, "TAKE_OFF", "GUIDED_PRACTICE_MCQ", "HIGH_ERROR"),
    ("F-SNOW_PLOW", F_SNOW_PLOW, "SNOW_PLOW", "STEP_BACK", "DECELERATING"),
    ("F-AIM", F_AIM, "AIM", "CHALLENGE_UP", "MASTERED"),
    ("F-AIM_CLOSE", F_AIM_CLOSE, "AIM", "KEEP_GOING", "MASTERED"),
    ("F-MID_LEVEL", F_MID_LEVEL, "MID_LEVEL", "STEP_BACK", "SLOW_GROWTH"),
    ("F-SURFACE", F_SURFACE, "SURFACE", "SLICE_BACK", "SLOW_GROWTH"),
    ("F-DOWNHILL", F_DOWNHILL, "DOWNHILL", "STEP_BACK", "DECELERATING"),
    ("F-LANDING", F_LANDING, "LANDING", "SLICE_BACK", "SLOW_GROWTH"),
    ("F-DIVE", F_DIVE, "DIVE", "GUIDED_PRACTICE_MCQ", "SLOW_GROWTH"),
    ("F-UPHILL", F_UPHILL, "UPHILL", "DRILL_ERRORS", "HIGH_ERROR"),
    ("F-CROSSOVER_JAWS", F_CROSSOVER_JAWS, "CROSSOVER_JAWS", "KEEP_GOING", "OK_PROGRESS"),
    ("F-DATA_TOO_THIN", F_DATA_TOO_THIN, "MID_LEVEL", "REQUEST_MORE_DATA", "DATA_TOO_THIN"),
    ("F-MULTIPLE_VALUES_PER_DAY", F_MULTIPLE_VALUES_PER_DAY, "SNOW_PLOW", "STEP_BACK", "DECELERATING"),
])

async def test_learning_picture_parameterized(name, fixture_data, expected_picture, expected_action, expected_status):
    results = [make_quiz_result_for_day(day, correct, incorrect) for day, correct, incorrect in fixture_data]
    base_result = results[-1]
    async def mock_get(url, *args, **kwargs):
        print(f"Mock GET request to: {url}")
        if "threads" in url:
            return make_response_with_json({
                "current_module_id": "mod-2",
                "module_ids": ["mod-1", "mod-2"]
            }, url)
        elif "quizzes" in url:
            return make_response_with_json({
                "quiz_id": base_result.quiz_id,
                "title": "Test Quiz",
                "description": "Test Quiz Description",
                "questions": [
                {
                    "question_id": "q1",
                    "knowledgebit_id": "kb1",
                    "user_level": "university",
                    "type": "flash_card",
                    "text": "Vad är fotosyntes?",
                    "hidden_text": "Fotosyntes är processen där växter omvandlar ljusenergi till kemisk energi.",
                    "alternatives": [] 
                },
                {
                    "question_id": "q2",
                    "knowledgebit_id": "kb2",
                    "user_level": "university",
                    "type": "flash_card",
                    "text": "Vad är cellandning?",
                    "hidden_text": "Cellandning är processen där celler bryter ned glukos för att frigöra energi.",
                    "alternatives": []
                },
                {
                    "question_id": "q",
                    "knowledgebit_id": "kb3",
                    "user_level": "university",
                    "type": "flash_card",
                    "text": "Vad är cellandning?",
                    "hidden_text": "Cellandning är processen där celler bryter ned glukos för att frigöra energi.",
                    "alternatives": []
                }
            ],
        "knowledgebits_ids": ["kb1", "kb2", "kb3"]
            }, url)
        elif "/students/student-1" in url:
            return make_response_with_json({
                "user_level": "university"
            }, url)
        else:
            raise ValueError(f"Unhandled URL: {url}")
    mock_client = AsyncMock()
    mock_client.get.side_effect = mock_get

    with patch("progression.core.analysis.fetch_filtered_history", return_value=results):
        result = await analyse(base_result, mock_client)
    print(f"▶ {name}")
    print(f"Picture: {result.learning_picture}, Status: {result.status}, Action: {result.action}")

    assert result.learning_picture == expected_picture
    assert result.status == expected_status
    assert result.action == expected_action

@pytest.mark.asyncio
@pytest.mark.parametrize("name, fixture_data, expected_picture, expected_action, expected_status", [
    ("F-JAWS", F_JAWS, "JAWS", "KEEP_GOING", "OK_PROGRESS"),
    ("F-CLIMB", F_CLIMB, "CLIMB", "KEEP_GOING", "OK_PROGRESS"),
    ("F-TAKE_OFF", F_TAKE_OFF, "TAKE_OFF", "GUIDED_PRACTICE_MCQ", "HIGH_ERROR"),
])

# Helper function to create a mock response with JSON data
def make_quiz_result_for_day(
    day_offset: int,
    correct: int,
    incorrect: int,
    quiz_id="quiz-1",
    thread_id="thread-1",
    student_id="student-1",
) -> QuizResultRead:
    submitted_at = datetime.now(timezone.utc) - timedelta(days=day_offset)
    return QuizResultRead(
        result_id=f"res-{day_offset}",
        quiz_id=quiz_id,
        thread_id=thread_id,
        student_id=student_id,
        score=Score(correct=correct, incorrect=incorrect, percentage=0.0),
        quiz_status=QuizStatus.current,
        quiz_mode=QuizMode.test,
        question_type=QuestionType.flash_card,
        is_timed=True,
        time_limit=60,
        fluency_goal=30,
        feedback_level=Level.low,
        total_questions=correct + incorrect,
        answers=[],
        correct_answers={},
        time_per_question=[],
        submitted_at=submitted_at,
        started_at=submitted_at - timedelta(minutes=1)
    )
