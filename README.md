📚 Book Recommendation System

A Book Recommendation Web Application built using Flask (backend) and HTML + CSS (frontend).
It recommends books based on similarity and also showcases popular books in an interactive grid layout.

🚀 Features

🔍 Search by Book Title → Get book recommendations instantly.

📖 Popular Books Section → Displays most popular books.

🎨 Interactive Frontend → Clean UI with book background images.

⚡ Pre-trained Models → Fast predictions using pickle files.

🛠️ Tech Stack

Python 3.11+

Flask (for backend API + frontend rendering)

Pickle (for loading pre-trained datasets)

HTML + CSS (for frontend design)
📊 Dataset

The project uses preprocessed book datasets stored in .pkl format:

books.pkl → Book details (title, author, image URL, etc.)

popular.pkl → Most popular books

pt.pkl → Pivot table (user-item matrix)

similarity_scores.pkl → Pre-computed similarity matrix
