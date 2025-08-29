# AMUST Library Management System

A Python-based library management system that helps users browse, search, and borrow engineering books using advanced text similarity algorithms.

## Features

- **📚 Book Browsing**: View all available engineering books in a formatted table
- **🔍 Smart Search**: Find books using TF-IDF vectorization and cosine similarity for accurate results
- **📖 Borrow Management**: Track book borrowing with student names and dates
- **📊 Statistics**: View borrowed books statistics
- **💾 Data Persistence**: Save borrowing records to CSV files

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd amust-library
```

2. Install required dependencies:
```bash
pip install pandas scikit-learn
```

3. Ensure you have the `Engineering_Books.csv` file in the project directory

## Usage

Run the application:
```bash
python library_manager.py
```

### Menu Options:
1. **View Books**: Display all available books in a formatted table
2. **Search & Borrow**: Search for books and borrow them
3. **Show Stats**: Display statistics of borrowed books
4. **Exit**: Close the application

## How It Works

### Search Algorithm
The system uses TF-IDF vectorization to convert book titles into numerical representations, then calculates cosine similarity between the search query and all book titles to find the most relevant matches.

### Borrowing System
- Students can borrow up to 3 books simultaneously
- Borrowing records are saved in `borrow_books.csv`
- Each record includes book details, student name, date, and return status

## File Structure

```
amust-library/
├── library_manager.py  # Main application
├── Engineering_Books.csv  # Book database
└── borrow_books.csv   # Borrow records (created automatically)
```

## Dependencies

- pandas: Data manipulation and analysis
- scikit-learn: Machine learning algorithms for text processing
- Python Standard Library: os, datetime

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

---
