import sqlite3
DATABASE = "database/database.db"

def get_connection():
    return sqlite3.connect(DATABASE)

# Prompt History Table

def create_prompt_history_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompt_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature TEXT,
            prompt TEXT,
            user_input TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# Chat History Table

def create_chat_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature TEXT,
            user_input TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# Feedback Table

def create_feedback_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature TEXT,
            feedback TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# Initialize Database

def initialize_database():

    create_prompt_history_table()
    create_chat_table()
    create_feedback_table()

# Save Prompt History

def save_prompt_history(
        feature,
        prompt,
        user_input
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prompt_history
        (
            feature,
            prompt,
            user_input
        )
        VALUES (?, ?, ?)
    """, (
        feature,
        prompt,
        user_input
    ))

    conn.commit()
    conn.close()


# Get Prompt History

def get_prompt_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM prompt_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# Save Chat

def save_chat(
        feature,
        user_input,
        response
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chat_history
        (
            feature,
            user_input,
            response
        )
        VALUES (?, ?, ?)
    """, (
        feature,
        user_input,
        response
    ))

    conn.commit()
    conn.close()

# Get Chat History


def get_chat_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM chat_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# Save Feedback

def save_feedback(
        feature,
        feedback
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO feedback
        (
            feature,
            feedback
        )
        VALUES (?, ?)
    """, (
        feature,
        feedback
    ))

    conn.commit()
    conn.close()


# Get Feedback

def get_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM feedback
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

# Dashboard Statistics

def create_users_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def initialize_database():

    create_prompt_history_table()
    create_chat_table()
    create_feedback_table()
    create_users_table()


def save_user(username, password_hash):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    """, (username, password_hash))

    conn.commit()
    conn.close()


def get_user_by_username(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, password_hash
        FROM users
        WHERE username = ?
    """, (username,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_total_chats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM chat_history
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_total_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM feedback
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_positive_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM feedback
        WHERE feedback='Yes'
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count

def get_total_prompts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM prompt_history
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count

def get_most_used_feature():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT feature,
               COUNT(*) as total
        FROM prompt_history
        GROUP BY feature
        ORDER BY total DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()

    return result

def get_recent_activities():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT feature,
               user_input,
               timestamp
        FROM prompt_history
        ORDER BY id DESC
        LIMIT 5
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_feature_usage():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT feature,
               COUNT(*)
        FROM prompt_history
        GROUP BY feature
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_feedback_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT feedback,
               COUNT(*)
        FROM feedback
        GROUP BY feedback
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_daily_usage():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DATE(timestamp),
               COUNT(*)
        FROM prompt_history
        GROUP BY DATE(timestamp)
        ORDER BY DATE(timestamp)
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")