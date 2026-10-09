
import sqlite3
import hashlib
from datetime import datetime

DB_NAME = "agile_data_guard.db"


def create_database():
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_text TEXT NOT NULL,
                fingerprint TEXT UNIQUE NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


def make_fingerprint(text):
    normalized = " ".join(text.casefold().split())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def add_record(text):
    text = text.strip()

    if not text:
        return "Rejected: empty data."

    fingerprint = make_fingerprint(text)

    try:
        with sqlite3.connect(DB_NAME) as connection:
            connection.execute(
                """INSERT INTO records
                   (original_text, fingerprint, created_at)
                   VALUES (?, ?, ?)""",
                (text, fingerprint, datetime.now().isoformat(timespec="seconds"))
            )
        return "Added successfully: " + text

    except sqlite3.IntegrityError:
        return "Duplicate detected: " + text


def show_records():
    with sqlite3.connect(DB_NAME) as connection:
        rows = connection.execute(
            "SELECT id, original_text, created_at FROM records ORDER BY id"
        ).fetchall()

    if not rows:
        print("No records stored yet.")
        return

    print("\n--- Verified Unique Records ---")
    for record_id, text, created_at in rows:
        print(f"{record_id}. {text} | {created_at}")


def main():
    create_database()
    print("=== Agile Data Guard ===")

    while True:
        print("\n1. Add data")
        print("2. View unique records")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Enter data: ")
            print(add_record(text))

        elif choice == "2":
            show_records()

        elif choice == "3":
            print("Data Guard closed.")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
