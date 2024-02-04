"""Module to count words in a file given """
import argparse
import time

def open_file(file_name):
    """Open file and convert in a array

    Parameters
    ----------
    file_name : str
        file name to load

    Returns
    -------
    list
        array with values in the file
    """
    try:
        with open(file_name, "r", encoding="utf8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied when trying to read {file_name}.")
        return []
    array = text.split()
    return array


def output_file(statistics):
    """Create output text file

    Parameters
    ----------
    statistics : dictionary
        dictionary with statistics values of the file 
    """

    with open("WordCountResults.txt","w",encoding="utf8") as f:
        f.write(str(statistics))
def count_words(array):
    """Count words in an array

    Parameters
    ----------
    array : list
        array with words in the file

    Returns
    -------
    dictionary
        dictionary with counting words
    """
    dict_result = {}
    for word in array:
        if word in dict_result:
            dict_result[word] += 1
        else:
            dict_result[word] = 1

    dict_result = dict(sorted(dict_result.items(), key=lambda x: x[1], reverse=True))
    return dict_result

def main():
    """Run compute statistics with the file given
    """
    start_time = time.time()
    parser = argparse.ArgumentParser(
        description='Compute a counting from a file containing words.')
    parser.add_argument('-f', '--file', type=str, required=True, help="File that contains words")
    args = parser.parse_args()

    file_name = args.file
    array = open_file(file_name)
    result = count_words(array)
    output_file(result)
    end_time = time.time()
    execute_time = end_time - start_time
    print(f"Execute time: {execute_time} seconds")
    print("Results:", result)

if __name__ == "__main__":
    main()
