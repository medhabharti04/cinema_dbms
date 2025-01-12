import sqlite3

# Function to create the movie and show timings tables
def MovieData():
    con = sqlite3.connect("movie1.db") 
    cur = con.cursor()
    
    # Create the Movies table
    cur.execute("""CREATE TABLE IF NOT EXISTS Movies (
                    id INTEGER PRIMARY KEY, 
                    Movie_ID TEXT,
                    Movie_Name TEXT,
                    Release_Date TEXT,
                    Director TEXT,
                    Cast TEXT,
                    Budget TEXT,
                    Duration TEXT,
                    Rating TEXT)""")
    
    # Create the Show_Timings table
    cur.execute("""CREATE TABLE IF NOT EXISTS Show_Timings (
                    id INTEGER PRIMARY KEY, 
                    Movie_ID TEXT,
                    Theater_Name TEXT,
                    Show_Date TEXT,
                    Show_Time TEXT)""")
    
    con.commit()
    con.close()

# Function to add movie records
def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("INSERT INTO Movies VALUES (NULL, ?,?,?,?,?,?,?,?)", 
                (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()

# Function to add show timings
def AddShowTiming(Movie_ID, Theater_Name, Show_Date, Show_Time):
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("INSERT INTO Show_Timings VALUES (NULL, ?, ?, ?, ?)", 
                (Movie_ID, Theater_Name, Show_Date, Show_Time))
    con.commit()
    con.close()

# Function to view all movie records
def ViewMovieData():
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("SELECT * FROM Movies")
    rows = cur.fetchall()
    con.close()    
    return rows

# Function to view show timings for movies
def ViewShowTimings():
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("SELECT * FROM Show_Timings")
    rows = cur.fetchall()
    con.close()    
    return rows

# Initialize the database and tables
MovieData()

# Add 20 movie records
movies = [
    ("M001", "Inception", "2010-07-16", "Christopher Nolan", "Leonardo DiCaprio, Joseph Gordon-Levitt", "160M", "148 min", "9.0/10"),
    ("M002", "Interstellar", "2014-11-07", "Christopher Nolan", "Matthew McConaughey, Anne Hathaway", "165M", "169 min", "8.6/10"),
    ("M003", "The Dark Knight", "2008-07-18", "Christopher Nolan", "Christian Bale, Heath Ledger", "185M", "152 min", "9.0/10"),
    ("M004", "Avatar", "2009-12-18", "James Cameron", "Sam Worthington, Zoe Saldana", "237M", "162 min", "7.8/10"),
    ("M005", "Titanic", "1997-12-19", "James Cameron", "Leonardo DiCaprio, Kate Winslet", "200M", "195 min", "7.9/10"),
    ("M006", "The Shawshank Redemption", "1994-09-23", "Frank Darabont", "Tim Robbins, Morgan Freeman", "25M", "142 min", "9.3/10"),
    ("M007", "Pulp Fiction", "1994-10-14", "Quentin Tarantino", "John Travolta, Uma Thurman", "8M", "154 min", "8.9/10"),
    ("M008", "Forrest Gump", "1994-07-06", "Robert Zemeckis", "Tom Hanks, Robin Wright", "55M", "142 min", "8.8/10"),
    ("M009", "The Matrix", "1999-03-31", "Lana Wachowski, Lilly Wachowski", "Keanu Reeves, Laurence Fishburne", "63M", "136 min", "8.7/10"),
    ("M010", "Gladiator", "2000-05-05", "Ridley Scott", "Russell Crowe, Joaquin Phoenix", "103M", "155 min", "8.5/10"),
    ("M011", "The Godfather", "1972-03-24", "Francis Ford Coppola", "Marlon Brando, Al Pacino", "6M", "175 min", "9.2/10"),
    ("M012", "The Godfather: Part II", "1974-12-20", "Francis Ford Coppola", "Al Pacino, Robert De Niro", "13M", "202 min", "9.0/10"),
    ("M013", "Schindler's List", "1993-12-15", "Steven Spielberg", "Liam Neeson, Ralph Fiennes", "22M", "195 min", "9.0/10"),
    ("M014", "The Lion King", "1994-06-24", "Roger Allers, Rob Minkoff", "Matthew Broderick, Jeremy Irons", "45M", "88 min", "8.5/10"),
    ("M015", "The Avengers", "2012-05-04", "Joss Whedon", "Robert Downey Jr., Chris Evans", "220M", "143 min", "8.0/10"),
    ("M016", "Avengers: Endgame", "2019-04-26", "Anthony Russo, Joe Russo", "Robert Downey Jr., Chris Evans", "356M", "181 min", "8.4/10"),
    ("M017", "Jurassic Park", "1993-06-11", "Steven Spielberg", "Sam Neill, Laura Dern", "63M", "127 min", "8.2/10"),
    ("M018", "Harry Potter and the Sorcerer's Stone", "2001-11-16", "Chris Columbus", "Daniel Radcliffe, Rupert Grint", "125M", "152 min", "7.6/10"),
    ("M019", "The Lord of the Rings: The Fellowship of the Ring", "2001-12-19", "Peter Jackson", "Elijah Wood, Ian McKellen", "93M", "178 min", "8.8/10"),
    ("M020", "The Lord of the Rings: The Return of the King", "2003-12-17", "Peter Jackson", "Elijah Wood, Ian McKellen", "94M", "201 min", "9.0/10")
]

for movie in movies:
    AddMovieRec(*movie)

# Add some sample show timings
show_timings = [
    ("M001", "Cineplex A", "2024-12-05", "10:00 AM"),
    ("M001", "Cineplex B", "2024-12-05", "01:00 PM"),
    ("M002", "Theater X", "2024-12-05", "05:00 PM"),
    ("M003", "Cineplex A", "2024-12-06", "11:00 AM"),
    ("M004", "Theater Y", "2024-12-06", "03:00 PM")
]

for timing in show_timings:
    AddShowTiming(*timing)

# View movie data and show timings
print("Movies:")
print(ViewMovieData())

print("\nShow Timings:")
print(ViewShowTimings())
