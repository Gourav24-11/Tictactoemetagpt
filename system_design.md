## Implementation approach:
To implement the diary app, we will use the Flask framework for the backend and HTML/CSS/JavaScript for the frontend. Flask is a lightweight and flexible web framework that allows us to quickly build web applications. We will also use SQLAlchemy as the ORM (Object-Relational Mapping) tool to interact with the database. For password encryption, we will use the bcrypt library.

## Python package name:
```python
"diary_app"
```

## File list:
```python
[
    "main.py",
    "models.py",
    "views.py",
    "templates/index.html",
    "templates/entry.html",
    "templates/edit.html",
    "templates/settings.html",
    "static/css/style.css",
    "static/js/script.js"
]
```

## Data structures and interface definitions:
```mermaid
classDiagram
    class User{
        +id: int
        +username: str
        +password: str
        +entries: List[Entry]
        +create_entry(title: str, content: str) -> Entry
        +get_entry(entry_id: int) -> Entry
        +edit_entry(entry_id: int, title: str, content: str) -> Entry
        +delete_entry(entry_id: int) -> None
    }
    class Entry{
        +id: int
        +title: str
        +content: str
        +user_id: int
        +user: User
    }
    class DiaryApp{
        +users: List[User]
        +create_user(username: str, password: str) -> User
        +get_user(user_id: int) -> User
        +authenticate(username: str, password: str) -> bool
        +encrypt_password(password: str) -> str
        +verify_password(password: str, hashed_password: str) -> bool
    }
    User "1" -- "N" Entry: has
    DiaryApp "1" -- "N" User: has
```

## Program call flow:
```mermaid
sequenceDiagram
    participant Main as Main
    participant DiaryApp as App
    participant User as User
    participant Entry as Entry
    participant bcrypt as Bcrypt

    Main->>+App: Create user
    App->>+User: create_user(username, password)
    User-->>-App: User object
    App-->>-Main: User object

    Main->>+App: Authenticate user
    App->>+User: authenticate(username, password)
    User-->>-App: True/False
    App-->>-Main: True/False

    Main->>+App: Create entry
    App->>+User: get_user(user_id)
    User-->>-App: User object
    App->>+User: create_entry(title, content)
    User-->>-App: Entry object
    App-->>-Main: Entry object

    Main->>+App: Get entry
    App->>+User: get_user(user_id)
    User-->>-App: User object
    App->>+User: get_entry(entry_id)
    User-->>-App: Entry object
    App-->>-Main: Entry object

    Main->>+App: Edit entry
    App->>+User: get_user(user_id)
    User-->>-App: User object
    App->>+User: edit_entry(entry_id, title, content)
    User-->>-App: Entry object
    App-->>-Main: Entry object

    Main->>+App: Delete entry
    App->>+User: get_user(user_id)
    User-->>-App: User object
    App->>+User: delete_entry(entry_id)
    User-->>-App: None
    App-->>-Main: None
```

## Anything UNCLEAR:
The requirements are clear to me.