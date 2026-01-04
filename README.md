# Dictionary-Project
#### Video Demo: https://youtu.be/7qf88CIqZhY
#### Description: The project starts by prompting the user to select their preferred language from a list including English, French and Hindi. Once a user selects a language, they are presented with five options. Five menu options are displayed to the user once a language is chosen. The fifth option allows the user to terminate the program.


By utilizing a sophisticated multilingual dictionary tool, users are able to store and categorise words from various languages. The developers had the task of creating a dictionary system which could be used in a very straightforward manner, in the form of a command line tool, and support various languages. The programme allows users to check the meanings of words and users can add their own word lists, and modify their stored entries using an easy to navigate interface.


To begin with, users are able to select their preferred language for the application. Upon choosing a language which is not at present within the database, the system will create a new language entry. Below is a list of the options that are displayed by the program: they include adding a word to a dictionary, looking up a word, checking all words that have been stored, changing the language being used, or quitting the program. Each language has its own vocabulary database which helps in the separation of storage areas.


Before a new word is entered into the dictionary, the programme checks whether it matches any of the current dictionary entries. All programmatic data is written to a file, this ensures that data integrity is maintained even after the program has shut down. Users can look up and expand upon previously stored entries in this database which houses all of their entries.


The program is structured in a logical way which separates the programme's features into distinct functions, thus improving the clarity and modularity of the code. This facilitates future modification. By accessing the main menu the user can interact with the system. The application has a collection of helper routines which accomplish three main tasks, these are word insertion and translation and word display and language selection. The testing process uses Pytest to automate the process of checking that all the systems are working as expected in terms of language selection, word insertion, translation quality and error detection.


This project demonstrates the practical application of Python in real-world software development scenarios, through its implementation of file input/output operations and data structures as well as its use of object-oriented programming principles and software testing techniques. The program is also designed to be expanded in the future, enabling sentence to sentence translations and a connection to online translation programmes. This will also be integrated with a user friendly interface. The application displays good quality coding standards due to its function in a production environment.


1. Translate a word - Take the word the user entered and translates it in the selected language
2. Add new word - Adds a new word with its meaning to the list, if the word is already there, it will print "Word already exists" to avoid duplications.
3. List all words - Shows all the words that are already saved
4. Change language - Switch languages from hindi to french and vice versa
5. Quit - Exit the program

