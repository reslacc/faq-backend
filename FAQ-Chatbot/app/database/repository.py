import sqlite3
from pathlib import Path

# Get project root (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database path
DB_PATH = BASE_DIR / "data" / "faq.db"


def get_answer_by_intent(intent: str) -> str:
    """
    Retrieve FAQ answer by intent.
    Returns default message if intent not found.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT answer FROM faq WHERE intent = ?",
            (intent,)
        )

        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0]
        else:
            return "Sorry, I could not find information about that topic."

    except sqlite3.Error as e:
        return f"Database error: {str(e)}"