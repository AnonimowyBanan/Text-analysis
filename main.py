import typer
import os
import pathlib
import re
import string

def truncate(n, decimals=0):
    """
        A function that rounds a given number and return it
    """
    multiplier = 10 ** decimals
    
    return int(n * multiplier) / multiplier

def save_output(out: str):
    """
        A function that creates a file, opens a connection to it, and writes output to it
    """
    with open('output.txt', 'w') as fileWrite:
        fileWrite.write(out)
    fileWrite.close()

    return True

def open_file(name: str):
    """
        A function that opens a connection to a file saved when starting the application
    """
    with open(name, 'r') as file:
        data = file.read().lower()
    file.close()

    return data

def file_validation(name: str):
    """
        A function that checks if in directory entered file exist
    """
    status = False
    path = str(pathlib.Path().resolve())
    path += "/" + name
    if os.path.exists(path):
        status = True

    return status

def count_words(data: str):
    """
        A function that returns the number of words in a string variable
    """
    words = len(data.split())

    return words

def count_sentences(data: str):
    """
        A function that returns the number of sentences in a string variable using regex
    """
    regex = "([^\.\?\!]*)[\.\?\!]"
    sList = re.findall(regex, data)

    return len(sList)

def list_unique_words(data: str):
    """
        The function counting the number of unique occurrences of a given word returns words in the list with and without repetitions
    """
    newData = data.translate(str.maketrans('', '', string.punctuation))
    l1 = newData.split()
    wList = list(set(newData.split()))
    resultList = {}
    for i in wList:
        resultList[i] = l1.count(i)
    repeatList = dict(sorted(resultList.items(), key=lambda item: item[1], reverse=True))
    uniqueList = {key:val for key, val in repeatList.items() if val == 1}

    return repeatList, uniqueList

def percentage_occurrence(data: dict, range: int):
    pResult = {}
    i = 0
    for key, value in data.items():
        if i >= range:
            break
        pResult[key] = truncate((value / sum(data.values())) * 100)
        i += 1

    return pResult

def print_CLI(out: str):
    print(out)

def create_string(cWords: int, cSentences: int, uWords: dict, pOccurence: dict):
    output = f"""
--- Text analize ---
Words: {cWords}
Centences: {cSentences}
Unique words:
"""
    for key in uWords:
        output += f"{key} - "
    output += "\nPercentage of occurrence of the most frequent words in the text:\n"
    for key, value in pOccurence.items():
        output += f"\t- {key} : {value}%\n"

    return output

app = typer.Typer()

@app.command()
def start(name: str, save: bool = False, display: bool = True):
    if file_validation(name):
        data = open_file(name)
        repList, uniqList = list_unique_words(data)
        output = create_string(count_words(data), count_sentences(data), uniqList, percentage_occurrence(repList, 10))
        if(display):
            print_CLI(output)
        if(save):
            if save_output(output):
                print("Output file saved")
    else:
        print("File: Error")
        exit


if __name__ == "__main__":
    app()
