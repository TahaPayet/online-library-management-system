from app import create_app, db
from app.models import Book

app = create_app()

books = [
    # --- Fiction ---
    {"title": "The Kite Runner", "author": "Khaled Hosseini", "isbn": "9781594631931", "category": "Fiction", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9781594631931-L.jpg"},
    {"title": "A Thousand Splendid Suns", "author": "Khaled Hosseini", "isbn": "9781594489501", "category": "Fiction", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781594489501-L.jpg"},
    {"title": "Beloved", "author": "Toni Morrison", "isbn": "9781400033416", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9781400033416-L.jpg"},
    {"title": "The Color Purple", "author": "Alice Walker", "isbn": "9780156028356", "category": "Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780156028356-L.jpg"},
    {"title": "Middlemarch", "author": "George Eliot", "isbn": "9780141439549", "category": "Fiction", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780141439549-L.jpg"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "isbn": "9780143035008", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780143035008-L.jpg"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "isbn": "9780199232765", "category": "Fiction", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780199232765-L.jpg"},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "isbn": "9780374528379", "category": "Fiction", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780374528379-L.jpg"},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "isbn": "9780060883287", "category": "Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780060883287-L.jpg"},
    {"title": "Love in the Time of Cholera", "author": "Gabriel Garcia Marquez", "isbn": "9780307389732", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780307389732-L.jpg"},
    {"title": "The Sun Also Rises", "author": "Ernest Hemingway", "isbn": "9780743297332", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780743297332-L.jpg"},
    {"title": "A Farewell to Arms", "author": "Ernest Hemingway", "isbn": "9780684801469", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780684801469-L.jpg"},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck", "isbn": "9780143039433", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780143039433-L.jpg"},
    {"title": "East of Eden", "author": "John Steinbeck", "isbn": "9780142004234", "category": "Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780142004234-L.jpg"},
    {"title": "Invisible Man", "author": "Ralph Ellison", "isbn": "9780679732761", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780679732761-L.jpg"},
    {"title": "Their Eyes Were Watching God", "author": "Zora Neale Hurston", "isbn": "9780061350344", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780061350344-L.jpg"},
    {"title": "Never Let Me Go", "author": "Kazuo Ishiguro", "isbn": "9781400078776", "category": "Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781400078776-L.jpg"},
    {"title": "The Remains of the Day", "author": "Kazuo Ishiguro", "isbn": "9780679731726", "category": "Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780679731726-L.jpg"},
    {"title": "Atonement", "author": "Ian McEwan", "isbn": "9780385721790", "category": "Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780385721790-L.jpg"},
    {"title": "Normal People", "author": "Sally Rooney", "isbn": "9781984822185", "category": "Fiction", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781984822185-L.jpg"},
 
    # --- Science Fiction ---
    {"title": "Ender's Game", "author": "Orson Scott Card", "isbn": "9780812550702", "category": "Science Fiction", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780812550702-L.jpg"},
    {"title": "Foundation", "author": "Isaac Asimov", "isbn": "9780553293357", "category": "Science Fiction", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780553293357-L.jpg"},
    {"title": "I, Robot", "author": "Isaac Asimov", "isbn": "9780553294385", "category": "Science Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780553294385-L.jpg"},
    {"title": "Neuromancer", "author": "William Gibson", "isbn": "9780441569595", "category": "Science Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780441569595-L.jpg"},
    {"title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "isbn": "9780441478125", "category": "Science Fiction", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780441478125-L.jpg"},
    {"title": "Slaughterhouse-Five", "author": "Kurt Vonnegut", "isbn": "9780440180296", "category": "Science Fiction", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780440180296-L.jpg"},
    {"title": "The Martian", "author": "Andy Weir", "isbn": "9780804139021", "category": "Science Fiction", "copies": 8, "rating": 4.90, "cover": "https://covers.openlibrary.org/b/isbn/9780804139021-L.jpg"},
    {"title": "Project Hail Mary", "author": "Andy Weir", "isbn": "9780593135204", "category": "Science Fiction", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780593135204-L.jpg"},
    {"title": "Recursion", "author": "Blake Crouch", "isbn": "9781524759780", "category": "Science Fiction", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781524759780-L.jpg"},
    {"title": "Dark Matter", "author": "Blake Crouch", "isbn": "9781101904244", "category": "Science Fiction", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781101904244-L.jpg"},
 
    # --- Fantasy ---
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "isbn": "9780553381689", "category": "Fantasy", "copies": 8, "rating": 4.90, "cover": "https://covers.openlibrary.org/b/isbn/9780553381689-L.jpg"},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "isbn": "9780756404079", "category": "Fantasy", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780756404079-L.jpg"},
    {"title": "The Way of Kings", "author": "Brandon Sanderson", "isbn": "9780765326355", "category": "Fantasy", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780765326355-L.jpg"},
    {"title": "Mistborn: The Final Empire", "author": "Brandon Sanderson", "isbn": "9780765311788", "category": "Fantasy", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780765311788-L.jpg"},
    {"title": "American Gods", "author": "Neil Gaiman", "isbn": "9780060558123", "category": "Fantasy", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780060558123-L.jpg"},
    {"title": "Good Omens", "author": "Terry Pratchett & Neil Gaiman", "isbn": "9780060853983", "category": "Fantasy", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780060853983-L.jpg"},
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "isbn": "9780066238500", "category": "Fantasy", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780066238500-L.jpg"},
    {"title": "Eragon", "author": "Christopher Paolini", "isbn": "9780375826696", "category": "Fantasy", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780375826696-L.jpg"},
    {"title": "The Sword of Kaigen", "author": "M.L. Wang", "isbn": "9781733245401", "category": "Fantasy", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9781733245401-L.jpg"},
    {"title": "Six of Crows", "author": "Leigh Bardugo", "isbn": "9781627792127", "category": "Fantasy", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9781627792127-L.jpg"},
 
    # --- Mystery ---
    {"title": "And Then There Were None", "author": "Agatha Christie", "isbn": "9780062073488", "category": "Mystery", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780062073488-L.jpg"},
    {"title": "Murder on the Orient Express", "author": "Agatha Christie", "isbn": "9780062073501", "category": "Mystery", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780062073501-L.jpg"},
    {"title": "The Hound of the Baskervilles", "author": "Arthur Conan Doyle", "isbn": "9780141034546", "category": "Mystery", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780141034546-L.jpg"},
    {"title": "In the Woods", "author": "Tana French", "isbn": "9780143113492", "category": "Mystery", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780143113492-L.jpg"},
    {"title": "The Big Sleep", "author": "Raymond Chandler", "isbn": "9780394758282", "category": "Mystery", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780394758282-L.jpg"},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "isbn": "9781250301697", "category": "Mystery", "copies": 8, "rating": 4.90, "cover": "https://covers.openlibrary.org/b/isbn/9781250301697-L.jpg"},
    {"title": "Big Little Lies", "author": "Liane Moriarty", "isbn": "9780425274866", "category": "Mystery", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780425274866-L.jpg"},
 
    # --- Thriller ---
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "isbn": "9781594634024", "category": "Thriller", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9781594634024-L.jpg"},
    {"title": "The Bourne Identity", "author": "Robert Ludlum", "isbn": "9780553260113", "category": "Thriller", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780553260113-L.jpg"},
    {"title": "No Country for Old Men", "author": "Cormac McCarthy", "isbn": "9780307387134", "category": "Thriller", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780307387134-L.jpg"},
    {"title": "The Pelican Brief", "author": "John Grisham", "isbn": "9780440214984", "category": "Thriller", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780440214984-L.jpg"},
    {"title": "Along Came a Spider", "author": "James Patterson", "isbn": "9780316693936", "category": "Thriller", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780316693936-L.jpg"},
    {"title": "I Am Pilgrim", "author": "Terry Hayes", "isbn": "9781476717494", "category": "Thriller", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781476717494-L.jpg"},
 
    # --- Horror ---
    {"title": "It", "author": "Stephen King", "isbn": "9781501142970", "category": "Horror", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781501142970-L.jpg"},
    {"title": "Pet Sematary", "author": "Stephen King", "isbn": "9781501156700", "category": "Horror", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781501156700-L.jpg"},
    {"title": "Misery", "author": "Stephen King", "isbn": "9780451169525", "category": "Horror", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780451169525-L.jpg"},
    {"title": "Interview with the Vampire", "author": "Anne Rice", "isbn": "9780345409645", "category": "Horror", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780345409645-L.jpg"},
    {"title": "House of Leaves", "author": "Mark Z. Danielewski", "isbn": "9780375703768", "category": "Horror", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780375703768-L.jpg"},
    {"title": "The Haunting of Hill House", "author": "Shirley Jackson", "isbn": "9780143039983", "category": "Horror", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780143039983-L.jpg"},
 
    # --- Young Adult ---
    {"title": "The Giver", "author": "Lois Lowry", "isbn": "9780544336261", "category": "Young Adult", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780544336261-L.jpg"},
    {"title": "Holes", "author": "Louis Sachar", "isbn": "9780440228257", "category": "Young Adult", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780440228257-L.jpg"},
    {"title": "The Perks of Being a Wallflower", "author": "Stephen Chbosky", "isbn": "9781451696196", "category": "Young Adult", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781451696196-L.jpg"},
    {"title": "Speak", "author": "Laurie Halse Anderson", "isbn": "9780312674397", "category": "Young Adult", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780312674397-L.jpg"},
    {"title": "The Outsiders", "author": "S.E. Hinton", "isbn": "9780142407332", "category": "Young Adult", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780142407332-L.jpg"},
    {"title": "Tuesdays with Morrie", "author": "Mitch Albom", "isbn": "9780767905923", "category": "Young Adult", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780767905923-L.jpg"},
    {"title": "The House on Mango Street", "author": "Sandra Cisneros", "isbn": "9780679734772", "category": "Young Adult", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780679734772-L.jpg"},
 
    # --- Romance ---
    {"title": "Sense and Sensibility", "author": "Jane Austen", "isbn": "9780141439662", "category": "Romance", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780141439662-L.jpg"},
    {"title": "Emma", "author": "Jane Austen", "isbn": "9780141439587", "category": "Romance", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780141439587-L.jpg"},
    {"title": "Outlander", "author": "Diana Gabaldon", "isbn": "9780440212560", "category": "Romance", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780440212560-L.jpg"},
    {"title": "Me Before You", "author": "Jojo Moyes", "isbn": "9780143124542", "category": "Romance", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780143124542-L.jpg"},
    {"title": "The Notebook", "author": "Nicholas Sparks", "isbn": "9780446605236", "category": "Romance", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780446605236-L.jpg"},
    {"title": "It Ends with Us", "author": "Colleen Hoover", "isbn": "9781501110368", "category": "Romance", "copies": 8, "rating": 4.90, "cover": "https://covers.openlibrary.org/b/isbn/9781501110368-L.jpg"},
    {"title": "The Time Traveler's Wife", "author": "Audrey Niffenegger", "isbn": "9780156029438", "category": "Romance", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780156029438-L.jpg"},
 
    # --- History ---
    {"title": "The Rise and Fall of the Third Reich", "author": "William L. Shirer", "isbn": "9781451651683", "category": "History", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9781451651683-L.jpg"},
    {"title": "Homo Deus", "author": "Yuval Noah Harari", "isbn": "9780062464316", "category": "History", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780062464316-L.jpg"},
    {"title": "The Silk Roads", "author": "Peter Frankopan", "isbn": "9781101912379", "category": "History", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781101912379-L.jpg"},
    {"title": "SPQR: A History of Ancient Rome", "author": "Mary Beard", "isbn": "9781631492228", "category": "History", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9781631492228-L.jpg"},
    {"title": "The Crusades", "author": "Thomas Asbridge", "isbn": "9780060787288", "category": "History", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780060787288-L.jpg"},
    {"title": "1776", "author": "David McCullough", "isbn": "9780743226721", "category": "History", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780743226721-L.jpg"},
    {"title": "The Diary of a Young Girl (Definitive Edition)", "author": "Anne Frank", "isbn": "9780385473781", "category": "History", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780385473781-L.jpg"},
 
    # --- Science ---
    {"title": "The Origin of Species", "author": "Charles Darwin", "isbn": "9780140432053", "category": "Science", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780140432053-L.jpg"},
    {"title": "Cosmos", "author": "Carl Sagan", "isbn": "9780345539434", "category": "Science", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780345539434-L.jpg"},
    {"title": "The Double Helix", "author": "James D. Watson", "isbn": "9780743216302", "category": "Science", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780743216302-L.jpg"},
    {"title": "Surely You're Joking, Mr. Feynman!", "author": "Richard Feynman", "isbn": "9780393316049", "category": "Science", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780393316049-L.jpg"},
    {"title": "The Gene: An Intimate History", "author": "Siddhartha Mukherjee", "isbn": "9781476733524", "category": "Science", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9781476733524-L.jpg"},
    {"title": "Being Mortal", "author": "Atul Gawande", "isbn": "9780805095159", "category": "Science", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780805095159-L.jpg"},
    {"title": "The Emperor of All Maladies", "author": "Siddhartha Mukherjee", "isbn": "9781439170915", "category": "Science", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9781439170915-L.jpg"},
 
    # --- Psychology ---
    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "isbn": "9780807014271", "category": "Psychology", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780807014271-L.jpg"},
    {"title": "The Body Keeps the Score", "author": "Bessel van der Kolk", "isbn": "9780143127741", "category": "Psychology", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780143127741-L.jpg"},
    {"title": "Influence", "author": "Robert Cialdini", "isbn": "9780062937650", "category": "Psychology", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780062937650-L.jpg"},
    {"title": "Quiet: The Power of Introverts", "author": "Susan Cain", "isbn": "9780307352156", "category": "Psychology", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780307352156-L.jpg"},
    {"title": "Flow", "author": "Mihaly Csikszentmihalyi", "isbn": "9780061339202", "category": "Psychology", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780061339202-L.jpg"},
    {"title": "The Interpretation of Dreams", "author": "Sigmund Freud", "isbn": "9780465019779", "category": "Psychology", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780465019779-L.jpg"},
 
    # --- Self-Help ---
    {"title": "Atomic Habits", "author": "James Clear", "isbn": "9780735211292", "category": "Self-Help", "copies": 10, "cover": "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg"},
    {"title": "Deep Work", "author": "Cal Newport", "isbn": "9781455586691", "category": "Self-Help", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9781455586691-L.jpg"},
    {"title": "Mindset", "author": "Carol S. Dweck", "isbn": "9780345472328", "category": "Self-Help", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780345472328-L.jpg"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "isbn": "9780062457714", "category": "Self-Help", "copies": 8, "rating": 4.90, "cover": "https://covers.openlibrary.org/b/isbn/9780062457714-L.jpg"},
    {"title": "Ikigai", "author": "Hector Garcia & Francesc Miralles", "isbn": "9780143130727", "category": "Self-Help", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780143130727-L.jpg"},
    {"title": "Grit", "author": "Angela Duckworth", "isbn": "9781501111105", "category": "Self-Help", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781501111105-L.jpg"},
 
    # --- Business ---
    {"title": "Zero to One", "author": "Peter Thiel", "isbn": "9780804139298", "category": "Business", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780804139298-L.jpg"},
    {"title": "The Lean Startup", "author": "Eric Ries", "isbn": "9780307887894", "category": "Business", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780307887894-L.jpg"},
    {"title": "Good to Great", "author": "Jim Collins", "isbn": "9780066620992", "category": "Business", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780066620992-L.jpg"},
    {"title": "The Innovator's Dilemma", "author": "Clayton M. Christensen", "isbn": "9780062060242", "category": "Business", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780062060242-L.jpg"},
    {"title": "Thinking in Systems", "author": "Donella H. Meadows", "isbn": "9781603580557", "category": "Business", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781603580557-L.jpg"},
    {"title": "The Hard Thing About Hard Things", "author": "Ben Horowitz", "isbn": "9780062273208", "category": "Business", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780062273208-L.jpg"},
    {"title": "Shoe Dog", "author": "Phil Knight", "isbn": "9781501135927", "category": "Business", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781501135927-L.jpg"},
 
    # --- Biography / Autobiography ---
    {"title": "Educated", "author": "Tara Westover", "isbn": "9780399590504", "category": "Autobiography", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780399590504-L.jpg"},
    {"title": "Becoming", "author": "Michelle Obama", "isbn": "9781524763138", "category": "Autobiography", "copies": 8, "rating": 4.90, "cover": "https://covers.openlibrary.org/b/isbn/9781524763138-L.jpg"},
    {"title": "The Story of My Experiments with Truth", "author": "Mahatma Gandhi", "isbn": "9780807059098", "category": "Autobiography", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780807059098-L.jpg"},
    {"title": "Leonardo da Vinci", "author": "Walter Isaacson", "isbn": "9781501139154", "category": "Biography", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781501139154-L.jpg"},
    {"title": "Einstein: His Life and Universe", "author": "Walter Isaacson", "isbn": "9780743264747", "category": "Biography", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780743264747-L.jpg"},
    {"title": "Alexander Hamilton", "author": "Ron Chernow", "isbn": "9780143034759", "category": "Biography", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780143034759-L.jpg"},
    {"title": "The Autobiography of Malcolm X", "author": "Malcolm X & Alex Haley", "isbn": "9780345350688", "category": "Autobiography", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780345350688-L.jpg"},
 
    # --- Philosophy ---
    {"title": "Meditations", "author": "Marcus Aurelius", "isbn": "9780812968255", "category": "Philosophy", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780812968255-L.jpg"},
    {"title": "Thus Spoke Zarathustra", "author": "Friedrich Nietzsche", "isbn": "9780140441185", "category": "Philosophy", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780140441185-L.jpg"},
    {"title": "Beyond Good and Evil", "author": "Friedrich Nietzsche", "isbn": "9780679724659", "category": "Philosophy", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780679724659-L.jpg"},
    {"title": "The Republic", "author": "Plato", "isbn": "9780872201361", "category": "Philosophy", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780872201361-L.jpg"},
    {"title": "Nicomachean Ethics", "author": "Aristotle", "isbn": "9780872204645", "category": "Philosophy", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780872204645-L.jpg"},
    {"title": "Being and Nothingness", "author": "Jean-Paul Sartre", "isbn": "9780671867805", "category": "Philosophy", "copies": 3, "rating": 4.1, "cover": "https://covers.openlibrary.org/b/isbn/9780671867805-L.jpg"},
    {"title": "The Stranger", "author": "Albert Camus", "isbn": "9780679720201", "category": "Philosophy", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780679720201-L.jpg"},
 
    # --- Technology ---
    {"title": "The Mythical Man-Month", "author": "Frederick P. Brooks Jr.", "isbn": "9780201835953", "category": "Technology", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780201835953-L.jpg"},
    {"title": "Design Patterns", "author": "Gang of Four", "isbn": "9780201633610", "category": "Technology", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780201633610-L.jpg"},
    {"title": "You Don't Know JS", "author": "Kyle Simpson", "isbn": "9781491924464", "category": "Technology", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781491924464-L.jpg"},
    {"title": "The Linux Command Line", "author": "William Shotts", "isbn": "9781593279523", "category": "Technology", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9781593279523-L.jpg"},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "isbn": "9781593279929", "category": "Technology", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781593279929-L.jpg"},
    {"title": "The Phoenix Project", "author": "Gene Kim", "isbn": "9781942788294", "category": "Technology", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9781942788294-L.jpg"},
    {"title": "Cracking the Coding Interview", "author": "Gayle Laakmann McDowell", "isbn": "9780984782857", "category": "Technology", "copies": 7, "rating": 4.70, "cover": "https://covers.openlibrary.org/b/isbn/9780984782857-L.jpg"},
 
    # --- Mathematics ---
    {"title": "The Man Who Knew Infinity", "author": "Robert Kanigel", "isbn": "9780671750961", "category": "Mathematics", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780671750961-L.jpg"},
    {"title": "Fermat's Last Theorem", "author": "Simon Singh", "isbn": "9780385493628", "category": "Mathematics", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780385493628-L.jpg"},
    {"title": "How to Solve It", "author": "George Polya", "isbn": "9780691119663", "category": "Mathematics", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780691119663-L.jpg"},
    {"title": "The Art of Problem Solving Vol. 1", "author": "Sandor Lehoczky", "isbn": "9780977304561", "category": "Mathematics", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780977304561-L.jpg"},
 
    # --- Adventure ---
    {"title": "Into the Wild", "author": "Jon Krakauer", "isbn": "9780385486804", "category": "Adventure", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780385486804-L.jpg"},
    {"title": "Into Thin Air", "author": "Jon Krakauer", "isbn": "9780385494786", "category": "Adventure", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780385494786-L.jpg"},
    {"title": "The Call of the Wild", "author": "Jack London", "isbn": "9780486264721", "category": "Adventure", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780486264721-L.jpg"},
    {"title": "Treasure Island", "author": "Robert Louis Stevenson", "isbn": "9780141321004", "category": "Adventure", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780141321004-L.jpg"},
    {"title": "Around the World in 80 Days", "author": "Jules Verne", "isbn": "9780140449068", "category": "Adventure", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780140449068-L.jpg"},
    {"title": "Twenty Thousand Leagues Under the Sea", "author": "Jules Verne", "isbn": "9780140443530", "category": "Adventure", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780140443530-L.jpg"},
 
    # --- Drama ---
    {"title": "Death of a Salesman", "author": "Arthur Miller", "isbn": "9780140481341", "category": "Drama", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780140481341-L.jpg"},
    {"title": "A Raisin in the Sun", "author": "Lorraine Hansberry", "isbn": "9780679755333", "category": "Drama", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780679755333-L.jpg"},
    {"title": "The Glass Menagerie", "author": "Tennessee Williams", "isbn": "9780811214049", "category": "Drama", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780811214049-L.jpg"},
    {"title": "Hamlet", "author": "William Shakespeare", "isbn": "9780521618748", "category": "Drama", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780521618748-L.jpg"},
    {"title": "Macbeth", "author": "William Shakespeare", "isbn": "9780521618779", "category": "Drama", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780521618779-L.jpg"},
    {"title": "Romeo and Juliet", "author": "William Shakespeare", "isbn": "9780521618663", "category": "Drama", "copies": 6, "rating": 4.40, "cover": "https://covers.openlibrary.org/b/isbn/9780521618663-L.jpg"},
    {"title": "Othello", "author": "William Shakespeare", "isbn": "9780521618816", "category": "Drama", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780521618816-L.jpg"},
 
    # --- Religion / Spirituality ---
    {"title": "The Bible (NIV)", "author": "Various", "isbn": "9780310448914", "category": "Religion", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780310448914-L.jpg"},
    {"title": "The Quran (English Translation)", "author": "M.A.S. Abdel Haleem", "isbn": "9780192805486", "category": "Religion", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780192805486-L.jpg"},
    {"title": "Siddhartha", "author": "Hermann Hesse", "isbn": "9780553208849", "category": "Religion", "copies": 5, "rating": 4.61, "cover": "https://covers.openlibrary.org/b/isbn/9780553208849-L.jpg"},
    {"title": "The Bhagavad Gita", "author": "Anonymous", "isbn": "9780140449181", "category": "Religion", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780140449181-L.jpg"},
    {"title": "The Tao Te Ching", "author": "Laozi", "isbn": "9780061142666", "category": "Religion", "copies": 4, "rating": 4.2, "cover": "https://covers.openlibrary.org/b/isbn/9780061142666-L.jpg"},
]

with app.app_context():
    added = 0
    skipped = 0
    for b in books:
        if not Book.query.filter_by(isbn=b['isbn']).first():
            book = Book(
                title=b['title'],
                author=b['author'],
                isbn=b['isbn'],
                category=b['category'],
                cover_image=b['cover'],
                total_copies=b['copies'],
                available_copies=b['copies'],
                rating=b.get('rating', 4.0)
            )
            db.session.add(book)
            added += 1
        else:
            skipped += 1
    db.session.commit()
    print(f'Done. Added: {added} books. Skipped (already exist): {skipped}')