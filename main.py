import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data=pd.read_csv('Engineering_Books.csv')
class LibraryManager:
    def __init__(self,data):
        self.data = data
    
    def view_books(self,top_n=5):
        #if self.data.empty:
        #    print("No books available in the library.")
        #
        #else:
        #    
        #    for book in self.data.itertuples(index=False):
        #        print(f"Book Name   : {book[0]}")
        #        print(f"Author      : {book[1]}")
        #        print(f"Department  : {book[2]}")
        #        print("-" * 30)
        self.data.dropna(subset=['Book','Author','Dept Name'],inplace=True)
        self.data['Combined_text']=self.data['Book'] + ' ' + self.data['Author']
        self.vectorizer=TfidfVectorizer()
        self.book_vector=self.vectorizer.fit_transform(self.data['Combined_text'])
        
        search_query=input("")
        query=self.vectorizer.transform([department_name])
        similarity=cosine_similarity(query,self.book_vector).flatten()
        topic_indices=similarity.argsort[-top_n:][::-1]
        top_books=self.data.iloc[topic_indices]

        for book in top_books.itertuples(index=False):
            print(f"Book Name   : {book[0]}")

Manager=LibraryManager(data)
print("Welcome to the Library Manager!")
while True:
    print("\nMenu:")
    print("1. View all books")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        department_name=input("Enter your department name:")
        Manager.view_books(department_name)
    elif choice == '2':
        print("Exiting the Library Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")