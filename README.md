# Text Analysis
A simple text analysis program that allows you to enter text by specifying a filename that is in the same location as main.py.
The program allows you to:
- counting the number of words in the text
- counting the number of sentences in the text
- finding unique words in the text
- calculation of the percentage share of the 10 most frequently occurring words in the text

Necessary to run the program are:
- Python 3.7 or newer
- package Typer (`pip install typer`)

How to run program:
Once I have installed all the necessary packages, you need to move the text file to the same location as the executable file.

Then launch a terminal and type:
`python main.py "your file name".txt`

For example:
`python main.py test.txt`

Output in console:

![scc](https://user-images.githubusercontent.com/67584450/219050593-d1ce19fc-2515-4e67-8e89-2fced043f065.png)


You can also add additional parameters, such as:

`--save` - that will save your output in txt file (disabled by default)

`--no-display` - this will not display the output in the console (disabled by default)

For example:
`python main.py test.txt --save --no-display`

Output:

![2](https://user-images.githubusercontent.com/67584450/219051233-f7a42b0e-a833-464d-a928-79ac33445f3b.png)

Application has been tested on Debian 11 Bullseye

