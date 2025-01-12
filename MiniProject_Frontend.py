import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import Scrollbar, Listbox, VERTICAL

class MovieTheaterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Theater Booking")
        self.root.configure(bg="#2C3E50")
        self.root.geometry("700x650")  # Increase window size for the new design
        
        # Movie Data (ID, Name, Director, Actors, Budget, Duration, Rating)
        self.movies = [
            ('M001', 'The Dark Knight', 'Christopher Nolan', 'Christian Bale, Heath Ledger', '185M', '152 min', '9.0/10'),
            ('M002', 'Inception', 'Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt', '160M', '148 min', '8.8/10'),
            ('M003', 'The Matrix', 'Lana Wachowski, Lilly Wachowski', 'Keanu Reeves, Laurence Fishburne', '63M', '136 min', '8.7/10'),
            ('M004', 'The Godfather', 'Francis Ford Coppola', 'Marlon Brando, Al Pacino', '6M', '175 min', '9.2/10'),
            ('M005', 'Pulp Fiction', 'Quentin Tarantino', 'John Travolta, Uma Thurman', '8M', '154 min', '8.9/10'),
            ('M006', 'Forrest Gump', 'Robert Zemeckis', 'Tom Hanks, Robin Wright', '55M', '142 min', '8.8/10'),
            ('M007', 'The Shawshank Redemption', 'Frank Darabont', 'Tim Robbins, Morgan Freeman', '25M', '142 min', '9.3/10'),
            ('M008', 'The Lord of the Rings: The Fellowship of the Ring', 'Peter Jackson', 'Elijah Wood, Ian McKellen', '93M', '178 min', '8.8/10'),
            ('M009', 'The Godfather: Part II', 'Francis Ford Coppola', 'Al Pacino, Robert De Niro', '13M', '202 min', '9.0/10'),
            ('M010', 'Schindler\'s List', 'Steven Spielberg', 'Liam Neeson, Ben Kingsley', '22M', '195 min', '9.0/10'),
            ('M011', 'The Empire Strikes Back', 'Irvin Kershner', 'Mark Hamill, Harrison Ford', '18M', '124 min', '8.7/10'),
            ('M012', 'The Silence of the Lambs', 'Jonathan Demme', 'Jodie Foster, Anthony Hopkins', '19M', '118 min', '8.6/10'),
            ('M013', 'Fight Club', 'David Fincher', 'Brad Pitt, Edward Norton', '63M', '139 min', '8.8/10'),
            ('M014', 'Se7en', 'David Fincher', 'Brad Pitt, Morgan Freeman', '33M', '127 min', '8.6/10'),
            ('M015', 'The Avengers', 'Joss Whedon', 'Robert Downey Jr., Chris Evans', '220M', '143 min', '8.0/10'),
            ('M016', 'Avengers: Endgame', 'Anthony Russo, Joe Russo', 'Robert Downey Jr., Chris Evans', '356M', '181 min', '8.4/10'),
            ('M017', 'Jurassic Park', 'Steven Spielberg', 'Sam Neill, Laura Dern', '63M', '127 min', '8.2/10'),
            ('M018', 'Harry Potter and the Sorcerer\'s Stone', 'Chris Columbus', 'Daniel Radcliffe, Rupert Grint', '125M', '152 min', '7.6/10'),
            ('M019', 'The Lord of the Rings: The Return of the King', 'Peter Jackson', 'Elijah Wood, Ian McKellen', '94M', '201 min', '9.0/10'),
            ('M020', 'Star Wars: A New Hope', 'George Lucas', 'Mark Hamill, Harrison Ford', '11M', '121 min', '8.6/10'),
            ('M021', 'The Lion King', 'Roger Allers, Rob Minkoff', 'Matthew Broderick, James Earl Jones', '45M', '88 min', '8.5/10'),
            ('M022', 'Titanic', 'James Cameron', 'Leonardo DiCaprio, Kate Winslet', '200M', '195 min', '7.8/10'),
            ('M023', 'The Dark Knight Rises', 'Christopher Nolan', 'Christian Bale, Tom Hardy', '250M', '164 min', '8.4/10'),
            ('M024', 'Gladiator', 'Ridley Scott', 'Russell Crowe, Joaquin Phoenix', '103M', '155 min', '8.5/10'),
            ('M025', 'Interstellar', 'Christopher Nolan', 'Matthew McConaughey, Anne Hathaway', '165M', '169 min', '8.6/10')
        ]
        
        # Show Timings Data (Movie ID, Theater, Date, Time)
        self.timings = [
            ('M001', 'Cineplex A', '2024-12-05', '10:00 AM'),
            ('M001', 'Cineplex B', '2024-12-05', '01:00 PM'),
            ('M002', 'Theater X', '2024-12-05', '05:00 PM'),
            ('M003', 'Cineplex A', '2024-12-06', '11:00 AM'),
            ('M004', 'Theater Y', '2024-12-06', '03:00 PM'),
            ('M005', 'Cineplex A', '2024-12-07', '12:00 PM'),
            ('M006', 'Cineplex B', '2024-12-07', '02:30 PM'),
            ('M007', 'Theater X', '2024-12-07', '06:00 PM'),
            ('M008', 'Cineplex A', '2024-12-08', '01:00 PM'),
            ('M009', 'Theater Y', '2024-12-08', '04:00 PM'),
            ('M010', 'Cineplex A', '2024-12-09', '10:30 AM'),
            ('M011', 'Theater X', '2024-12-09', '01:00 PM'),
            ('M012', 'Cineplex B', '2024-12-09', '04:30 PM'),
            ('M013', 'Cineplex A', '2024-12-10', '11:15 AM'),
            ('M014', 'Theater Y', '2024-12-10', '02:45 PM'),
            ('M015', 'Cineplex A', '2024-12-11', '12:00 PM'),
            ('M016', 'Cineplex B', '2024-12-11', '03:00 PM'),
            ('M017', 'Theater X', '2024-12-11', '06:00 PM'),
            ('M018', 'Cineplex A', '2024-12-12', '10:00 AM'),
            ('M019', 'Cineplex B', '2024-12-12', '01:30 PM'),
            ('M020', 'Theater Y', '2024-12-12', '04:00 PM'),
            ('M021', 'Cineplex A', '2024-12-13', '11:00 AM'),
            ('M022', 'Theater X', '2024-12-13', '02:30 PM'),
            ('M023', 'Cineplex B', '2024-12-13', '06:00 PM'),
            ('M024', 'Theater Y', '2024-12-14', '12:00 PM'),
            ('M025', 'Cineplex A', '2024-12-14', '03:00 PM')
        ]
        
        # Title Section
        self.title_label = tk.Label(self.root, text="Welcome to Movie Theater Booking", font=("Arial", 24, "bold"), fg="#F39C12", bg="#2C3E50")
        self.title_label.pack(pady=20)
        
        # Catchy Subtitle
        self.subtitle_label = tk.Label(self.root, text="Your favorite movies, all in one place!", font=("Arial", 16), fg="#ECF0F1", bg="#2C3E50")
        self.subtitle_label.pack(pady=10)
        
        # Frame for Movie List and Scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Movie Listbox
        self.MovieList = Listbox(self.frame, height=10, width=50, font=("Arial", 14), selectmode=tk.SINGLE)
        self.MovieList.grid(row=0, column=0, padx=10, pady=8)

        # Scrollbar
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, command=self.MovieList.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns', pady=8)
        self.MovieList.config(yscrollcommand=self.scrollbar.set)

        # Add movie titles to listbox
        for movie in self.movies:
            self.MovieList.insert(tk.END, movie[1])

        # Add Buttons
        self.search_button = tk.Button(self.root, text="Search Movie", font=("Arial", 14), fg="#2C3E50", bg="#F39C12", command=self.search_movie)
        self.search_button.pack(pady=10)
        
        self.info_button = tk.Button(self.root, text="View Movie Information", font=("Arial", 14), fg="#2C3E50", bg="#F39C12", command=self.show_movie_info)
        self.info_button.pack(pady=10)
        
        self.book_button = tk.Button(self.root, text="Book Ticket", font=("Arial", 14), fg="#2C3E50", bg="#F39C12", command=self.book_ticket)
        self.book_button.pack(pady=10)
        
        self.update_button = tk.Button(self.root, text="Update Movie", font=("Arial", 14), fg="#2C3E50", bg="#F39C12", command=self.update_movie)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Movie", font=("Arial", 14), fg="#2C3E50", bg="#F39C12", command=self.delete_movie)
        self.delete_button.pack(pady=10)

    def search_movie(self):
        movie_name = simpledialog.askstring("Search Movie", "Enter the name of the movie:")
        if movie_name:
            matching_movies = [movie for movie in self.movies if movie_name.lower() in movie[1].lower()]
            if matching_movies:
                self.MovieList.delete(0, tk.END)
                for movie in matching_movies:
                    self.MovieList.insert(tk.END, movie[1])
            else:
                messagebox.showinfo("No Matches", "No movies found with that name.")

    def show_movie_info(self):
        selected_movie = self.MovieList.curselection()
        if not selected_movie:
            messagebox.showwarning("Selection Error", "Please select a movie to view information.")
            return
        movie_index = selected_movie[0]
        movie_details = self.movies[movie_index]
        movie_info = f"Movie Name: {movie_details[1]}\nDirector: {movie_details[2]}\nActors: {movie_details[3]}\nBudget: {movie_details[4]}\nDuration: {movie_details[5]}\nRating: {movie_details[6]}"
        messagebox.showinfo("Movie Information", movie_info)

    def book_ticket(self):
        selected_movie = self.MovieList.curselection()
        if not selected_movie:
            messagebox.showwarning("Selection Error", "Please select a movie to book a ticket.")
            return
        movie_index = selected_movie[0]
        movie_id = self.movies[movie_index][0]
        
        available_timings = [timing for timing in self.timings if timing[0] == movie_id]
        timing_options = [f"{timing[1]} | {timing[2]} | {timing[3]}" for timing in available_timings]
        
        if not timing_options:
            messagebox.showwarning("No Timings", "No available timings for this movie.")
            return
        
        timing_str = "\n".join(timing_options)
        timing_choice = simpledialog.askstring("Choose a Timing", f"Available timings:\n{timing_str}\n\nEnter the number of your preferred show:")
        
        try:
            timing_choice = int(timing_choice)
            if 1 <= timing_choice <= len(timing_options):
                selected_timing = available_timings[timing_choice - 1]
                messagebox.showinfo("Ticket Booked", f"Your ticket has been booked for {selected_timing[1]} at {selected_timing[2]}!")
            else:
                messagebox.showwarning("Invalid Choice", "Please select a valid timing number.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        except IndexError:
            messagebox.showwarning("Invalid Timing", "Please select a valid timing.")
        
    def update_movie(self):
        selected_movie = self.MovieList.curselection()
        if not selected_movie:
            messagebox.showwarning("Selection Error", "Please select a movie to update.")
            return
        movie_index = selected_movie[0]
        movie_id = self.movies[movie_index][0]

        movie_name = simpledialog.askstring("Update Movie", f"Enter the new name for movie {self.movies[movie_index][1]}:")
        if movie_name:
            self.movies[movie_index] = (movie_id, movie_name, *self.movies[movie_index][2:])
            messagebox.showinfo("Movie Updated", f"The movie {self.movies[movie_index][1]} has been updated.")
            self.refresh_movie_list()
        
    def delete_movie(self):
        selected_movie = self.MovieList.curselection()
        if not selected_movie:
            messagebox.showwarning("Selection Error", "Please select a movie to delete.")
            return
        movie_index = selected_movie[0]
        del self.movies[movie_index]
        messagebox.showinfo("Movie Deleted", "The selected movie has been deleted.")
        self.refresh_movie_list()

    def refresh_movie_list(self):
        self.MovieList.delete(0, tk.END)
        for movie in self.movies:
            self.MovieList.insert(tk.END, movie[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieTheaterApp(root)
    root.mainloop()
