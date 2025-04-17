# creating the lists
list= [1, 5, 10, 15, 20]
print(list)

print([True, False, False, "1"])

#list constructor
my_list = list(["Lists", "are", "useful!"])
print(my_list)

# list comphrehension
my_list = [num for num in range (1,6)]
print(my_list)

# indexing single line elements
my_list = [num for num in range (1,6)]
print(my_list)

element = my_list[2]
print(element)

# indexing portions of the lists
my_list = [num for num in range (1,6)]
my_list[0:4]

my_list = [1, 5, 10, 15, 20, 25, 30, 35, 40]
my_new_list = my_list[2:5]

print(my_new_list)

# negative indexing
my_list = [num for num in range (1,6)]

last_element = my_list[-1]
print(last_element)

# out of range index values
my_list = [num for num in range (1,6)]

try:
    element = my_list[10]
except IndexError:
    print("Index is out of range!")

# the list appending
my_list = [12, 19, 26, 23]
my_list.append(30)
print(my_list)

# the extend() method  ---- extend() is immensely useful for combining two lists or adding more than values all at once.
python_datatypes = ["lists"]
python_datatypes.extend(["tuples", "sets"])
print(python_datatypes)

# modify one element -- spelling sapphire
blue_shades = ['navy', 'sky blue', 'saphire', 'powder blue', 'teal', 'turquoise']
blue_shades[2] = 'sapphire'

print(blue_shades)

# modify mutiple elements 
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:2] = ['denim', 'aqua']

print(blue_shades)

# Different number of elements than the specified range
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:1] = ['denim', 'aqua']
print(blue_shades)

# On the other hand, when providing a larger range than the elements provided, the replacement covers the complete specified range, and the remaining elements shift accordingl
# Less elements than the specified range in Python
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:4] = ['denim', 'aqua']
print(blue_shades)

# Reassigning a list
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']

blue_shades = ['cobalt', 'azure', 'ice blue']
print(blue_shades)

# deleting the single element
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

del space_movies[2]
print(space_movies)

# deleting multi elements
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

del space_movies[1:3]
print(space_movies)

# removing by value
# by using a function remove()
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

space_movies.remove('Gravity')
print(space_movies)

# clearing the lists
# by using clear()
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
space_movies.clear()
print(space_movies)

# the pop method --- using pop()
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

removed_movie = space_movies.pop(2)
print("The removed movie is = " + removed_movie)
print(space_movies)

# list slicing ---  if u want to print the spectificed index valyes then u can use this
my_list = [1, 5, 10, 15, 20, 25, 30]
print(my_list[0:2])

#jupdating lists using lists slicing -- similar to modifing 
my_list = [1, 5, 10, 15, 20, 25, 30]

my_list[0:2] = 50, 55
print(my_list)

# inclusive and excluding 

#  the step parameter   syntax=[start:end:step]
my_list = [1, 5, 10, 15, 20, 25, 30]

my_list[0:2] = 50, 55
print(my_list)

# slicing from beginning   syntax = list name[:index] for beginning
my_list = [1, 5, 10, 15, 20, 25, 30]

slice_list_from_start = my_list[:4]
print(slice_list_from_start)

# slicing from a specific index till end syntax = list name[index:] till end
my_list = [1, 5, 10, 15, 20, 25, 30]

slice_list_till_end = my_list[4:]
print(slice_list_till_end)

# negative slicing 
# prints from last
my_list = [1, 5, 10, 15, 20, 25, 30]

last_three_elements = my_list[-3:]
print("Last three elements:", last_three_elements)

# 2
my_list = [1, 5, 10, 15, 20, 25, 30]

skip_every_second_from_end = my_list[-1:-6:-2]
print(skip_every_second_from_end)

# negative slicing for reversing
# syntax== list name[:: negative syntax]
my_list = [1, 5, 10, 15, 20, 25, 30]

reversed_list = my_list[::-1]
print(reversed_list)

#  list comphrehension - a list to be sub lsited qith a spcl quality
# Expression
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]

print(squares)

# condition
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)

# condition for short words
words = ["hoodie", "rivers", "cat", "monitor", "bag", "cup"]
short_words = [word for word in words if len(word) <= 5]

print(short_words)

# assignment to mutiply element
numbers = [1, 2, 3, 4, 5]
pairs = [(num, num * 2) for num in numbers]

print(pairs)

# transforming elements
songs = ['Neon Lights', 'Pieces', 'Everything']
uppercase_songs = [song.upper() for song in songs]

print(uppercase_songs)

# nested
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in my_matrix] for i in range(len(my_matrix[0]))]

print(transpose)

#the append(x) 
python_versions = ["Python 2", "Python 3"]
python_versions.append("Python 3.11")

print(python_versions)

# the extend
python_modules = ["NumPy", "Pandas"]

additional_modules = ["Matplotlib", "scikit-learn"]
python_modules.extend(additional_modules)

print(python_modules)

# insert
programming_languages = ["C", "Java", "Python", "Ruby"]
programming_languages.insert(1, "C++")

print(programming_languages)

# remove
frameworks = ["Django", "Flask", "Pyramid", "Flask"]
frameworks.remove("Flask")

# pop()
web_frameworks = ["Django", "Flask", "Pyramid", "FastAPI"]
removed_framework = web_frameworks.pop(2)

print(web_frameworks)

# clear
scripting_languages = ["Python", "Ruby", "Perl"]
scripting_languages.clear()

print(scripting_languages)

# index
languages = ["C", "C++", "Python", "Java", "Python"]
python_index = languages.index("Python")

print(python_index)

# count
version_numbers = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
python3_count = version_numbers.count(3)

print(python3_count)

# list sort
numeric_versions = [2.7, 3.0, 3.6, 3.7, 3.8, 3.9]
numeric_versions.sort()

print(numeric_versions)

# reverse
libraries = ["NumPy", "Pandas", "Matplotlib", "Scikit-Learn"]
libraries.reverse()

print(libraries)

# copy

libraries = ["NumPy", "Pandas", "Matplotlib", "Scikit-Learn"]
libraries.reverse()

print(libraries)