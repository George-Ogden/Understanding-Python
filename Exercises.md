# Exercises
Watching videos can give you an overview, but you only learn to code by writing, running, and debugging your own programs. Here are some exercises for each of the videos so that you can practise what you've learned:
## Lesson 01 - First Steps
1. Make sure you have Python installed!
2. Change what you print: what happens when you use numbers or change the text?
## Lesson 02 - Joke Machine
1. What happens when you change the order of input and output?
2. What happens if you remove the text in the brackets?
## Lesson 03 - Maths Made Easy
1. How can you tell whether the output of a calculation will be an integer, float (decimal) or boolean (true/false)?
2. `//` returns an integer when diving two other integers. What happens when the inputs are floats?
3. `"a" + "b" -> "ab"`. Which of the other operations work on strings?
4. What happens when you try to add a number and a string?
5. What happens when you try to add an integer and a float?
## Lesson 04 - Calculator
1. Another argument to `print` is `end`. What happens when you change the default value of `end`?
2. What happens when you try to divide by zero?
3. How does the program change if we use `int` to convert the input to an integer instead of `float`?
4. Which lines will still run if we remove the `float` from the input and leave the inputs as strings?
## Lesson 05 - Making Tea
1. Can you write a function to make coffee?
2. Can you write a function that calls itself?
3. What happens if you have two parameters with the same name? What about if you change which values have defaults and which don't?
4. What happens if you have two functions with the same name but different arguments?
5. What happens if you create a variable with the same name as a function?
## Lesson 06 - Bouncer
1. Try rewriting the calculator from lesson 4 to use an `if` statement in the input to only perform a single calculation, specified by the user.
2. [`match`](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) statements are new to Python. See if you can use them for the task above.
## Lesson 07 - Important Items
1. You can put anything in a list, including other lists. Try making a list of lists.
2. What happens if you try to access an item that doesn't exist in a list?
3. We only ever assign to values in the list. Can you create a variable that contains one of the values of the list?
4. Define a list `importantItems2 = importantItems`. What happens when you change `importantItems2`? How does this differ from changing `importantItems`?
5. You can get around this by using `importantItems2 = list(importantItems)` or `importantItems2 = importantItems.copy()`. Does this change the behaviour?
## Lesson 08 - Chopping and Changing
1. Python [lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) support some other methods. Try using some of them to change the list.
2. You can convert from a list of strings to a single string using `"<sep>".join(list)`. Try using this to print the list in a more readable format.
3. Can you use the join function to display a list of strings without the quotes (`["a", "b", "c"] -> [a, b, c]`)?
4. What happens when you append a list to itself?
## Lesson 09 - Python Turtle
1. Use your imagination to see what you can draw!
2. Write a method called `square` that draws a square of a given size.
3. Write a method called `hexagon` that draws a hexagon of a given size.
## Lesson 10 - N-agon
1. Write a method called `polygon` that draws a polygon of a given size and number of sides. Try using the line method from lesson 9 instead of forward and right.
2. Try doing this without calling `turtle.radians()`.
3. How can you draw a circle with the polygon methods?
## Lesson 11 - Guess My Number
1. Can you rewrite this without the state variable (just checking conditions based on min and max)?
2. Can you rewrite a `for` loop just using a `while` loop?
3. Using the [`time`](https://docs.python.org/3/library/time.html#time.sleep) module, can you write a less efficient version of `time.sleep()` using a `while` loop?
## Lesson 12 - Randomness
1. The [`random`](https://docs.python.org/3/library/random.html) module has a lot of other functions. Try playing around with some of them.
2. These numbers are actually pseudorandom and you can fix the seed to get the same sequence of numbers each time. Try using `random.seed()` to fix the seed and see what happens.
3. Can you simulate how many times it takes to get a 6 when rolling a dice? Repeat this 1000 times and see what the average is.
4. Try implementing a board game, such as ludo or snakes and ladders. Try different strategies and see which is most effective.
5. Try implementing a card game, such as blackjack or poker. Can you write a program that performs better than a random opponent or a human?
## Lesson 13 - Capital Cities
1. Can you write a program that asks the user for a capital city and tells them the country?
2. You can do a lot more with [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). Try playing around with some of the other methods.
3. What values are valid for the keys of dictionaries?
4. Create a function that takes in a person's data (name, age, height, etc.) and tells you which information is missing and which information is unnecessary.
5. The following code finds Fibonacci numbers but computes the solution to some values multiple times:
```python
def fib(n):
	if n <= 1:
		return 1
	elif n % 2 == 0:
		return fib(n//2) ** 2 + fib(n//2-1) ** 2
	else:
		return fib(n//2) * (fib(n//2+1) + fib(n//2-1))
```
Can you use a dictionary to store intermediate results and avoid recomputing the same value twice?
## Lesson 14 - Complex JSON
1. What data can you store in JSON?
2. How does JSON differ from Python dictionaries?
3. Have a look at [YAML](https://yaml.org/). How does it differ from JSON?
## Lesson 15 - Slicing and Dicing
1. Have a look at the [`slice`](https://docs.python.org/3/library/functions.html#slice) function. What are the advantages of using this over the slice notation?
2. How are `slice` and `range` related?
## Lesson 16 - Using Files
1. How can you use [`json.dump`](https://docs.python.org/3/library/json.html#json.dump), which is very similar to `json.dumps`?
2. What happens if you try to open a file that doesn't exist? What about writing to a file that doesn't exist? What about writing to a closed file?
3. [`pickle`](https://docs.python.org/3/library/pickle.html) is a module that can be used to save Python objects to a file. Try using it to save a list of dictionaries. What are the advantages/disadvantages of using `pickle` over `json`?
4. Write a program that can store birthdays. You should be able to add, edit, remove and see upcoming birthdays.
## Lesson 17 - OOP
1. [Python Turtle](https://docs.python.org/3/library/turtle.html) also has a `Screen` class. Try experimenting with some of these methods.
2. You can move each turtle individually. Try making a program that draws a square with each turtle moving at a different speed.
3. Try to draw a star where each turtle draws one line and they start and finish at the same time.
## Lesson 18 - Classy
1. Try creating a class that represents a person. Save it using `pickle` and load it again.
2. Create classes for different animals. Give each animal a method that makes a noise.
3. Create a class that represents a deck of cards. Give it a method that shuffles the deck. Give it a method that deals a card.
4. Try doing the previous exercise where each card is an object.
## Lesson 19 - Very Advanced Functions
1. Try writing a function that takes only `**kwargs` and checks that the keys are valid.
2. What happens when you change the order of the parameters? Can you still use `myfunc(foo=bar)` to make sure that the parameters are assigned correctly?
3. What are the limits on what you can use in a `lambda` function?
4. Python has a [`functools`](https://docs.python.org/3/library/functools.html) module that contains some useful functions. Try using some of them and writing your own versions of some of them.
5. The Python module [`inspect`](https://docs.python.org/3/library/inspect.html) has a [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature) class. Try using this to check that the parameters of a function are valid.
## Lesson 20 - Stringy Bits
1. Create a class and define a function `__repr__` that returns a string. Call `str()` on the object. What happens? What happens if you define a function `__str__` instead?
2. A new feature in Python is [f-strings](https://docs.python.org/3/tutorial/inputoutput.html). Try using these instead of `format`.
3. It can be useful for filenames to have a fixed number of digits, filled in with leading zeros. Try writing a function to do this and have a look at how you can do this with string formatting directly.
4. Try writing a pretty-print function for a dictionary. Make sure that it works for nested dictionaries and on a limited screen width.
## Lesson 21 - Inheritance
1. Try creating a class that inherits from `dict` and overrides the `__getitem__` method to return a default value if the key doesn't exist.
2. What happens if you try to inherit from multiple classes? What about if you try to inherit from a class that inherits from another class? Can you come up with examples that break Python's method resolution order?
3. Try creating a class that inherits from `list` and overrides the `__add__` method to add the elements of the lists together instead of concatenating them.
4. Create classes for different chess pieces and a class for the board. Give each piece a method that returns the squares it can move to and simulate a random chess game.
## Lesson 22 - Special Words
1. It's now common to use an Ellipsis (`...`) instead of `pass` in a function that hasn't been implemented yet. How does this differ from `pass`?
2. Some other interesting statements are [`assert`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assert_stmt), [`raise`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-raise_stmt) and [`delete`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-del_stmt). Try using these in your code.
## Lesson 23 - Sets
1. How much faster/slower are sets than lists? Benchmark this using the [`timeit`](https://docs.python.org/3/library/timeit.html) module.
2. Try writing your own version of a set where the elements are stored in order. What are the main difficulties you encounter?
## 	Lesson 24 - Advanced Imports
1. [`importlib`](https://docs.python.org/3/library/importlib.html) offers a lot more functionality than the `import` statement. Try using some of the other functions.
2. Python has a lot of conventions around how you should import modules. Find a convention that you find appealing and try to stick to it.
3. Try writing a module that imports itself. What happens?
4. Can you write two modules that import each other without an `ImportError`?
## Lesson 25 - Making Exceptions
1. Before exceptions, it was common to return a special value to indicate an error (such as -1). What are the advantages/disadvantages of this approach?
2. Create an `ArithmeticError` and add this to your calculator from lesson 4. Subclass your error with the different types of errors that can occur when doing arithmetic.
3. When doing internal testing, it is common to use [`assert`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assert_stmt) statements to generate errors. Try using these in your code.
## Lesson 26 - Error Handling
1. Create a menu utility that gets the user to select options by inputting numbers. At each step, handle incorrect inputs so the user tries only the previous step again.
2. Modify the menu code so that after 3 incorrect inputs, the program exits.
3. Write a program that can read a file and the user can add lines. If the user enters a blank line, the program should save and exit. If the user presses `Ctrl+C`, the program should save the file and exit. What other errors can occur and how should they be handled?
## Lesson 27 - Scope
1. As well as global, there is a `nonlocal` variable. Try using this in your code.
2. Define a function called `adder` that returns a function that adds a number to the input:
```python
>>> plus_2 = adder(2)
>>> plus_2(3)
5
```
How can you change the names of the variables to avoid conflicts?
3. Why does the following code not work?
```python
def counter(f):
	count = 0
	def wrapper(*args, **kwargs):
		count += 1
		print(count)
		return f(*args, **kwargs)
	return wrapper
```
How can you fix it?
```python
>>> print_counter = counter(print)
>>> print_counter("Hello")
1
Hello
>>> print_counter("World")
2
World
```
## Lesson 28 - Magic Methods
1. Python has lots of other [magic methods and some interesting attributes](https://docs.python.org/3/reference/datamodel.html). Try using some of them.
2. Write a `Matrix` class that can add and multiply matrices. You may also want to support other operators, such as `__repr__` and `__getitem__`.
3. Write a `Vector` class that is compatible with the `Matrix` class.
## Lesson 29 - Adding Decoration
1. You already wrote a `counter` decorator in lesson 27. Try writing some other decorators.
2. The [`functools`](https://docs.python.org/3/library/functools.html) module has a lot of useful decorators. Try using some of them.
3. Try writing your own code for some of the decorators in `functools`.
## Lesson 30 - Special Decorations
1. One decorator that I didn't cover is the [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod) decorator. Try using this in your code. What happens when you inherit from a class with a class method?
2. [Properties](https://docs.python.org/3/library/functions.html#property) also support setters and deleters. Define an `age` property based on their birthday that allows setting and deleting via modifying their birthday.
## Lesson 31 - Date and Time
1. How much jitter is there in the Python `sleep` method? (If I run `sleep(1)` 1000 times what are the minimum and maximum times?)
2. Write an extension of `timedelta` that takes in months.
## Lesson 32 - In a Pickle
1. What happens when you relead a file after changing the class definition? What about if you change the module name?
2. Write a class that can be pickled and unpickled. Define different versions so that when you change the class, you can still load the old version.
3. Try using the [`dill`](https://pypi.org/project/dill/) module instead of `pickle`. What are the advantages/disadvantages?
## Lesson 33 - Cool Stuff
1. Python ranges must have an end value. Write a class that accepts any value (including floats and infinity) and can be used as a range.
2. [`itertools`](https://docs.python.org/3/library/itertools.html) is a module that contains a lot of useful functions, try writing your own versions for some of them using generators.
3. List comprehensions don't just apply to lists. Try using them with a dictionary to make all the keys lowercase or a set to keep only even values.
4. try calling help on a function with a multiline comment (docstring). what happens?
5. multiline definitions are rarely used in practice. instead, you tend to use brackets. Try using the [`black`](https://pypi.org/project/black) formatter to see how it handles long lines.
## Lesson 34 - Bitwise Operators
1. Python stores negative integers in [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement). Try making a number positive/negative by only flipping the bits.
2. [Gray Code](https://en.wikipedia.org/wiki/Gray_code) is a way of representing numbers where only one bit changes between each number. Try writing a function that converts between Gray Code and natural numbers.
## Lesson 35 - Iterators
1. Convert the infinite range class from lesson 33 into an iterator.
2. Write a class that can be used as an iterator but also supports indexing.
3. Write an iterator that supports nested iteration of powers of 10:
```python
iterator = NestedTens()
for i in iterator:
	for j in iterator:
		print(i, j)
# 0, 0
# 0, 10
# 0, 20
# ...
# 0, 90
# 1, 0
# 1, 10
# ...
```
## Lesson 36 - NumPy
1. Without using loops, write code to generate a random integer between 0 and N-1 weighted by the square of the index.
2. Scale all numbers in an array so that the min is 0 and the max is 1.
3. Write a function that takes in a list of numbers and returns the index of the number closest to the mean.
4. Write a function that takes in a list of numbers and returns the index of the number closest to the median (try to do this without the builtin `numpy.median` function).
5. Using NumPy, create a histogram of the numbers in a list (the index is the number and the value is the number of times it appears in the list):
```
>>> histogram([1, 2, 4, 1, 2, 4, 0, 1, 1])
[1, 4, 2, 0, 2]
```
## Lesson 37 - pandas
1. Create two spreadsheets that are similar but one has a few changes. Use pandas to find the differences between the two.
2. Take a flat-file spreadsheet and use pandas to [normalise](https://en.wikipedia.org/wiki/Database_normalization) the data.
3. Download a dataset from the [internet](https://www.kaggle.com/datasets?fileType=csv&minUsabilityRating=9.00+or+higher) and use pandas to analyse it.
4. Remove anomalies from the dataset using pandas.
## Lesson 38 - Matplotlib
1. Try to make some of the charts look beautiful.
2. Using the dataset from lesson 37, create some charts that show interesting information.
3. Pandas has a [`plot`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html) method that can be used to plot data. Try creating some of these charts using matplotlib instead.
## Lesson 39 - Parsing Arguments
1. Modify the calculator from lesson 4 to take in arguments from the command line.
2. Write a program that reads data from an input file, performs some calculations and writes the results to an output file. Use the argparse module to specify the input, output files and parameters for the calculations.
3. Create a program to encode/encrypt and decode/decrypt a file. Use argparse for the input and output and give the user multiple modes [(sub-commands)](https://docs.python.org/3/library/argparse.html#sub-commands) to choose from.
4. Modify the program from lesson 26 to use argparse instead of input. Try to make it as user-friendly as possible.
5. Use argparse to verify the arguments of a program and print a help message if they are invalid.
## Lesson 40 - Gooey (GUI)
1. Modify the programs from lesson 39 to use a GUI instead of the command line.
2. Try using the widgets to make specific types of input easier.
3. Try using the progress bar while the program is running.
## Lesson 41 - Web Scraping
1. Start from an arbitrary website and try to find links off the page. Repeat this on the links you find and see if you can find a page that is frequently linked to.
2. Find all the pages on a website and count the number of times each word is used across the site.
3. Find all the pages on a website and count the number of times each image is used across the site.
4. Create a scraper to automatically convert a website from HTML into Markdown.
## Lesson 42 - Web Bots
1. Start on an arbitrary Wikipedia page and try to keep clicking on links to get to a random page.
2. Think of a task that you do routinely on the internet and try to automate it.
3. Try to book flights or order shopping with a bot.
4. Log into a social media account and download all the images and text to a local folder.
## Lesson 43 - SciPy
1. Try to find the roots of a polynomial using the [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) module.
2. Integrate a complicated function using the [`scipy.integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html) module.
3. Use the [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) module to generate random numbers from a distribution and plot the distribution.
4. Use the [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html) module to filter a noisy signal.
5. Use the [`scipy.linalg`](https://docs.scipy.org/doc/scipy/reference/linalg.html) module to solve a system of linear equations.
## Lesson 44 - APIs
1. The [Public APIs GitHub repo](https://github.com/public-apis/public-apis) provides a list of publicly available APIs. Try using some of them.
2. Try to find an API that requires authentication and use it.
## Lesson 45 - MySQL
1. Create a database of your favourite films and actors. Try to normalise the data.
2. Find a website that provides a lot of data and write a scraper to generate a database.
3. In lesson 37, you normalised a spreadsheet. Try to write a program that can convert a normalised database into a spreadsheet.
4. What queries can you perform on the database using SQL that are slower in Python?
## Lesson 46 - RegEx
1. Write a regex to match a valid email address.
2. Try to parse an HTML page using regex. Search for links, email addresses, phone numbers, etc.
3. Try to parse a CSV file using regex. Which columns are strings? Which are numbers?
## Lesson 47 - MongoDB
1. Try to convert the database from lesson 45 to MongoDB.
2. Convert some of the pandas and MySQL queries from lessons 37 and 45 to MongoDB.
## Lesson 48 - PyYAMl
1. Convert the JSON file from lesson 14 to YAML.
2. Convert the database from lesson 45 or 47 into YAML. If you're using a spreadsheet, what are the different ways you can represent the data?
## Lesson 49 - os
1. Try to write a program that can find all the files on your computer that contain a given string.
2. Write code that backs up all your files each day but only includes files that have changed and keeps backups for a week.
3. Try to use the os library to run an executable file and capture the output.
## Lesson 50 - Dynamic Execution
1. [`ast`](https://docs.python.org/3/library/ast.html) is a module that can be used to parse Python code. Try using it to parse a file and find all the functions that are defined.
2. [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval) is a function that can be used to evaluate a string as Python code. What are the advantages/disadvantages of using this over `eval`?
## Lesson 51 - Bytes
1. Convert a list of integers to a binary file and then load it again.
2. How could you reduce the size of a file if you knew that it only contained a-z, A-Z, 0-9, spaces and a dot? What's the smallest file you can make that contains the alphabet?
3. [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding) is a way of compressing data. Try to implement it to compress and decompress a file.
## Lesson 52 - Pillow
1. Generate code to iterate over all images in a folder and resize them to a given size.
2. Add a caption to the images based on the filename.
3. Try to find all the images on a website and download them. Convert them all to jpgs and resize them to a given size.
4. [Pillow](https://pillow.readthedocs.io/en/stable/index.html) provides a lot of other functionality. Try using some of it.
## Lesson 53 - OpenCV
1. Generate [Julia Sets](https://en.wikipedia.org/wiki/Julia_set) using OpenCV.
2. Use OpenCV modules to detect the foreground and background of an image.
3. Download an image with shapes on it and use OpenCV to detect the shapes and their positions.
4. Use OpenCV to animate a pendulum swinging.
## Lesson 54 - Threading
1. Try to write a program that uses threads to download multiple files at once.
2. Write a program to increment a counter using threads. How much faster is it than using a single thread?
3. Write a consumer and producer program where some threads add to a list and other threads take from the list and print the results. Make sure that the length is always less than 10.
## Lesson 55 - sys
1. Use sys to print the arguments passed to a program. Can you write a simpler version of ArgParse from lesson 39?
2. Use sys to write the stdout and stderr to separate files.
3. Run another program from your program using sys. How does this compare to using os?
4. Use sys to print the current memory usage of your program.
## Lesson 56 - paths
1. [`pathlib`](https://docs.python.org/3/library/pathlib.html) is a module that can be used to manipulate paths. Try using it to find all the files in a folder and its subfolders.
2. Delete cached files from your computer.
3. Rename files so that all the paths become dots, for example, `a/b/c/d.txt` becomes `a.b.c.d.txt`.
4. Sort files in a folder based on their extension, for example, `a.txt` and `b.jpg` become `txt/a.txt` and `jpg/b.jpg`.
## Lesson 57 - music
1. Trim silence from the start and end of an audio file.
2. Group all songs by artist and album and save them to appropriate folders.
3. Compress all songs without sacrificing too much quality.
## Lesson 58 - Wikipedia
1. Try to find the shortest path between two Wikipedia pages using only links on the page.
2. Find a page and see how many different languages it is available in.
3. Find a few similar pages and see how many references they have in common.
## Lesson 59 - emojis
1. Create a script to fill in the emojis in a file.
2. Write code to replace as many words in a file with emojis as possible.
3. Write a script to convert a file to emoji art.
## Lesson 60 - seaborn
1. Plot some of the charts from lesson 38 using seaborn.
2. Play around with the given datasets and see what interesting information you can find.
3. Use a heatplot to plot the correlations between different columns in a dataset.
## Lesson 61 - colorama
1. Modify the dataframe difference code from lesson 37 to highlight additions, deletions and changes in different colours.
2. Write code to print a coloured progress bar that changes colour as it progresses.
3. Display an image in the terminal using colour characters.
## Lesson 62 - cmaes
1. Use CMA-ES to find the minimum of a bounded polynomial.
2. Create a weighted heuristic for a game and use CMA-ES to find the best weights.
3. Create a race car simulator and use CMA-ES to find the best parameters for the car.
## Lesson 63 - semicolons in Python
1. Take a program that you've written and try to reduce the number of lines by using semicolons.
2. It's bad practice to use semicolons in Python. Write a piece of code to replace all unnecessary semicolons with newlines.
## Lesson 64 - Queueing
1. Write a program that downloads a lot of web pages. Place the urls in a queue and have multiple threads downloading and saving the pages.
2. Use a priority queue to implement [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).
3. Parallelise code from lesson 53 using one queue for the values that need computing and another queue for the results.
## Lesson 65 - statistics
1. Have a look at [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html). What can you do with scipy that you can't do with statistics?
2. Try to implement some of the functions in statistics using numpy.
## Lesson 66 - itertools
1. Try to implement some of the functions in itertools using generators.
2. Use an infinite iterator to create a loading spinner.
3. Create a function to flatten nested lists using itertools.
4. Simulate different games of the [lottery](https://en.wikipedia.org/wiki/Lottery_mathematics) and see how likely you are to win.
## Lesson 67 - functools
1. Try to write your own versions of the functions in functools.
2. Create a function to map each word to a unique integer. Use an LRU cache to speed up the function and see what the optimal cache size is.
3. Lots of the functions in the `math` module take multiple arguments. Write functions, such as `double` and `cube` that use `functools.partial` to create functions that only take one argument.
## Lesson 68 - zipfile
1. Write code to compress a folder to a zip file then delete the folder and to decompress a zip file and delete the zip file.
2. Write code to extract all the images from a zip file but no other files.
3. Transfer a file between two computers using a zip file. What level of compression minimises the total time?
## Lesson 69 - PySR
1. Find the best polynomial to fit the `log` function within a a given range.
2. See how changing the loss function affects the results. Which loss function gives the best results?
3. How can you modify the parameters to find the solution? Try combining CMAES from lesson 62 to find the best parameters.
## Lesson 70 - Help!
1. Docstrings often have a standardised format. Which format do you prefer? Try to stick to it in your code.
2. Add typing hints to some of the functions you've written in previous exercises.
3. The [`typing`](https://docs.python.org/3/library/typing.html) module has a lot of different types. Try using some of them in your code.
## Lesson 71 - PyInstaller
1. Try to create an executable for some of the programs you've written.
2. Try to make it look as professional as possible.
## Lesson 72 - getpass
1. Use the [`cryptography`](https://pypi.org/project/cryptography/) module to save the users password to a file securely.
2. Verify the hash of the password against a known hash. That way, you don't need to store the password at all.
## Lesson 73 - XML
1. Modify the XML from the lesson so that the default language is German and the English is provided as a translation.
2. Try to convert the JSON file from lesson 14 to XML.
3. Convert the YAML from lesson 48 into XML. Search for elements with certain properties using an XPath query.
## Lesson 74 - pynput
1. Create a program that acts as a text editor using pynput. Try to implement backspace and undo.
2. Use pynput to use the browser and download a file. Assume that all the buttons stay in the same place.
3. Create a GUI that counts the number of button presses in one second. How many can you do? How many can you do with pynput?
## Lesson 75 - Keys
1. Password protect your key file before allowing the user to use it.
2. Create a password manager that uses the key file to encrypt the passwords. How can you give different users access to different passwords?
## Lesson 76 - inspect
1. Create a wrapper that takes in a dictionary and only passes in the keys that are valid for a function.
2. Modify this function to have default arguments for the missing keys.
3. Use inspect to create a webpage that displays documentation and source code for a python module.
4. [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) provide a lot of boilerplate code. How could you write your own version of a dataclass?
## Lesson 77 - pytesseract
1. Take a screenshot of a webpage and use pytesseract to extract the text.
2. Extract the text from images of road signs.
3. What are the limits of pytesseract? What kinds of text can it not read?
## Lesson 78 - translate
1. Use the built in translate function to encode and decode a message. Can 
you write an automatic decryptor?
2. Translate some text with the `translate` module.
3. Use the [`googletrans`](https://pypi.org/project/googletrans/) module for translation. How does it compare `translate`?
## Lesson 79 - PrettyTable
1. Is it faster to perform the sorting in PrettyTable or Pandas?
2. Display a DataFrame in PrettyTable, highlighting the min and the max in each column.
3. Write code that takes a PrettyTable and converts it to a DataFrame.
## Lesson 80 - progress
1. Create an iterable that acts as a spinner until broken:
```python
for _ in Spinner():
	...
	if condition:
		break
```
2. Create a progress bar iterable to wrap around the range function:
```python
for _ in ProgressRangeBar(100):
	...
```
3. Make these two iterables customisable for the type of Spinner/Progress Bar.
## Lesson 81 - pendulum
1. Create a program that takes in a birthday and tells you how many days you have to wait.
2. Create a world clock that displays the time of different cities.
3. Display the date and time in different formats. What feels most natural?
## Lesson 82 - collections
1. Try to implement some of the functions in collections using dictionaries.
2. Create a class that inherits from `collections.UserDict` and overrides the `__getitem__` method to return a default value if the key doesn't exist.
3. Create a class that inherits from `collections.UserList` and overrides the `__getitem__` method to extend the list and fill with `None` when out of range.
## Lesson 83 - Flask
1. Create a flask app that supports multiple users logging in to view a personalised page.
2. Create a flask app that acts as a search engine for a user's files.
3. Create a flask app that allows users to upload files and view them.
4. Create a flask app that stores all of the user's interactions in a database and displays an analysis of their behaviour.
## Lesson 84 - unittest
1. Create test cases for the calculator from lesson 4.
2. Create test cases for the functions in lesson 37.
3. Unittest supports [mocking](https://docs.python.org/3/library/unittest.mock.html). Write test cases for a function that uses an external API and mock the API.
4. [`pytest`](https://pypi.org/project/pytest/) adds additional functionality to unittest. Try using it instead of and alongside unittest.
## Lesson 85 - matching
1. Create a pretty-print function for JSON that uses pattern matching to display the data in a more readable format.
2. Create a reverse function for a list that uses pattern matching and recursion. (Don't use the builtin `reversed` function.)
3. Using the matrix multiplication function from lesson 18, create a function that uses pattern matching to multiply scalars, vectors and matrices.
## Lesson 86 - PDFKit
1. Write a program to automatically turn a markdown document into a PDF.
2. Write a program that checks the weather forecast and produces a report as a PDF.
3. Write some utility scripts to combine PDFs, delete pages, etc.
## Lesson 87 - socket
1. Connect two computers and send messages between them.
2. Create a chatroom that allows multiple users to connect and send messages.
3. Create a server that sends work to multiple clients and collects the results.
## Lesson 88 - Advanced Numeric Types
1. Create safe arithmetic operators that raise `ValueError`s when the operation would raise a `TypeError`. Do this without using `try`/`except`.
2. Create a `mint` class that does arithmetic modulo a prime number.
3. Use the decimal class to find an approximation of pi.
##  Lesson 89 - metaclasses
1. Create a metaclass that checks that all the methods in a class have a docstring.
2. Modify the `mint` class from lesson 88 to use a metaclass to check that all inputs to functions are integers.
## Lesson 90 - email
1. Create a program to take in a dataframe and send personalised emails to the recipients.
2. Create a program to send an email to yourself when a program finishes running.
3. Python also has an [`IMAP`](https://docs.python.org/3/library/imaplib.html) module. Try using this to read and respond to emails automatically.
## Lesson 91 - Gmail
1. Create a program to add labels to emails based on their subject and content.
2. Create a program to reply automatically to emails based on a condition.
3. Send and receive zip files via email and automatically download and extract them.
## Lesson 92 - abc
1. Create an abstract class `Saveable` that allows you to `object.save(filename)`.
2. Create an abstract `Configurable` class that allows you to `Cls.from_config(config)`. Also create a `Config` class that can be used to store the configuration.
## Lesson 93 - tweepy
1. Find who your most common friends of friends are that you aren't friends with on Twitter.
2. Find the most common words in your tweets.
3. Tweet a random joke or inspirational quote every day.
4. Send yourself a message when someone tweets about you.
## Lesson 94 - tqdm
1. Create a program that waits a random amount of time during the loop and displays a progress bar. How accurate is the prediction?
2. Create nested for loops and display a progress bar for each loop. How can you make sure that the progress bars are displayed correctly?
3. Have multiple threads performing different tasks and display a progress bar for each task.
4. Have multiple threads performing the same task with a shared progress bar.
## Lesson 95 - MIDIs
1. Jazz up Für Elise with different musical features.
2. [Pretty MIDI](https://pypi.org/project/pretty_midi/) is an alternative library for working with MIDI files. How does the interface compare?
3. Create a program to combine two MIDI files into one in a way that sounds good.
## Lesson 96 - PyTorch
1. Try downloading FashionMNIST and training a neural network to classify the images. This dataset is much harder than MNIST but how well can you do?
2. PyTorch has a lot of [tutorials](https://pytorch.org/tutorials/). Try following them and getting better at using the framework.
## Lesson 97 - TensorFlow
1. Try using your improved neural network from lesson 96 to classify the images in TensorFlow.
2. TensorFlow has a lot of [tutorials](https://www.tensorflow.org/tutorials). Try following them and getting better at using the framework.
3. [`jax`](https://pypi.org/project/jax/) is starting to replace TensorFlow. Try using it instead of TensorFlow.
## Lesson 98 - manim
1. Manim has a lot of features. Try using some of them.
2. Create a video that explains a mathematical concept.
3. Create a video that explains a programming concept.
## Lesson 99 - The Zen of Python
1. There are lots of style guides and formatters for Python. Try using some of them and see which one you prefer.
2. Try taking some of your earlier code and refactoring it to be more Pythonic.
3. [GitHub](https://github.com) is a website that allows you to share code online. Have a look at some source code done by professionals and see how you can improve your code.
4. Try contributing to a GitHub project.