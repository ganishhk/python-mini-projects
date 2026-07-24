# 🎬 Movie Collection Manager

A command-line Movie Collection Manager built with **Python**, **Object-Oriented Programming (OOP)**, **JSON**, and **File Handling**.

This project allows users to manage their personal movie collection by adding, searching, viewing, updating, and deleting movies while automatically saving data to a JSON file.

---

## 🚀 Features

- ➕ Add a new movie
- 📋 View all movies
- 🔍 Search movies by ID, Title, or Genre
- ⭐ Mark movies as Watched or Unwatched
- ❌ Delete movies
- 💾 Automatic JSON data saving
- 🔄 Automatic data loading on startup
- ⚠️ Exception handling for invalid Movie ID input

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling

---

## 📂 Project Structure

```
Movie Collection Manager/
│
├── main.py
├── movie.py
├── movie_manager.py
├── movies.json
└── README.md
```

---

## 💡 Concepts Practiced

- Classes & Objects
- Constructors
- Encapsulation
- File Handling
- JSON Serialization & Deserialization
- CRUD Operations
- Data Persistence
- Loops & Conditionals
- Functions & Methods
- Debugging
- Program Design

---

## 📖 How It Works

1. The program loads movie data from `movies.json`.
2. JSON data is converted into Movie objects.
3. All operations are performed on Movie objects in memory.
4. Whenever data changes, the objects are converted back into dictionaries.
5. The updated data is saved back to `movies.json`.

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-link>
```

2. Navigate to the project folder

```bash
cd movie-collection-manager
```

3. Run the program

```bash
python main.py
```

---

## 📚 What I Learned

While building this project, I learned:

- Designing programs using OOP
- Separating responsibilities into different classes and methods
- Reading and writing JSON files
- Managing application data in memory
- Converting Objects ↔ Dictionaries
- Debugging logical errors
- Organizing a Python project

---

## 👨‍💻 Author

**Ganish Kumar**

Currently learning Python, SQL, Data Analytics, and building projects to strengthen software development skills.

⭐ If you found this project interesting, feel free to fork the repository and give it a star.