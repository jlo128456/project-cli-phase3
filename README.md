
#Personal Library CLI

A command-line interface (CLI) app for managing your personal book library. Built using Python, SQLAlchemy ORM, and Click.

---

##Features

- List all books with their authors and genres
- Create or reset tables using ORM
- Seed the database with initial sample data
- Modular structure (easy to extend)

---

##Tech Stack

- Python 3.8+
- Click for CLI
- SQLAlchemy for ORM
- SQLite (default)
- VS Code + virtualenv for development

---

##Project Structure

```
personal_library_cli/
├── library.py               # Entry point for CLI commands
├── cli.py                   # CLI definitions using Click
├── lib/
│   ├── helpers.py           # Shared utilities
│   └── db/
│       ├── models.py        # SQLAlchemy ORM models
│       ├── session.py       # Engine + session factory
│       └── seed.py          # Seeding helper
├── requirements.txt         # Python dependencies
└── README.md
```

---

##Getting Started in VS Code

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd personal_library_cli
```

### 2. Open the folder in VS Code

```bash
code .
```

> Ensure you have the **Python extension** installed in VS Code.

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

Then activate it:

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set the Interpreter in VS Code

Press `Ctrl+Shift+P` → search for **Python: Select Interpreter** → choose `.venv` path.

---

##Usage

Run commands like:

```bash
python library.py create-tables --seed
python library.py list-books
```

### CLI Commands

| Command         | Description                            |
|-----------------|----------------------------------------|
| `create-tables` | Create/reset DB schema with `--seed`   |
| `list-books`    | Display all books in the library       |

---

##Using Pipenv Instead of venv

Prefer `pipenv` for dependency and virtual environment management? Here's how:

###Install dependencies

```bash
pipenv install click sqlalchemy
```

This creates a `Pipfile` and `Pipfile.lock` with the required packages.

###Activate the pipenv shell

```bash
pipenv shell
```

This will drop you into a shell using the isolated virtual environment managed by Pipenv.

###Run CLI commands from the shell

```bash
python library.py create-tables --seed
python library.py list-books
```

###Example `Pipfile`

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[packages]
click = "*"
sqlalchemy = "*"

[requires]
python_version = "3.8"
```

---

##Example Output

```bash
ID   Title                          Published    Author
--------------------------------------------------------------
1    The Hobbit                     1937-09-21   J. R. R. Tolkien
2    1984                           1949-06-08   George Orwell
```

---

## Contact

Made by **Jeffrey Lo**  
Email: j.lo128456@gmail.com

---

## License

MIT License
