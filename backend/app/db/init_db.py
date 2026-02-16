from app.db.session import get_conn

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  status TEXT NOT NULL,
  priority TEXT NOT NULL,
  effort_sp INTEGER NOT NULL,
  dependencies_json TEXT NOT NULL,
  created_at TEXT NOT NULL
);
"""

def main():
    with get_conn() as conn:
        conn.execute(SCHEMA)
        conn.commit()
    print("DB initialized.")

if __name__ == "__main__":
    main()
