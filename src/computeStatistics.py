import argparse
import time

def open_file(file_name):
    """
    Open a file and return its contents as a list of strings.
    
    Parameters:
        file_name (str): The path to the file to be opened.
    
    Returns:
        list: A list of strings where each string is an item from the file.
    """
    with open(file_name, "r") as f:
        text = f.read()
    
    array = text.split()
    return array
def is_number(s):
    """
    Check if a string represents a number, including negative and floating point numbers.
    
    Parameters:
        s (str): The string to check.
    
    Returns:
        bool: True if the string is a number, False otherwise.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def validate_type(array):
    """
    Convert a list of strings to floats where possible, ignoring non-numeric values.
    
    Parameters:
        array (list): A list of strings to be validated and converted.
    
    Returns:
        list: A list of floats converted from numeric strings in the original list.
    """
    array_numeric = []
    for value in array:
        if is_number(value):
            array_numeric.append(float(value))
        else:
            print(f"Value non numeric found {value} is ignored")
    return array_numeric

def sqrt(value):
    """
    Calculate the square root of a given number.
    
    Parameters:
        value (float): The number to calculate the square root for.
    
    Returns:
        float: The square root of the given number.
    """
    return value ** (1/2)

def mean(array):
    """
    Calculate the mean of a list of numbers.
    
    Parameters:
        array (list): The list of numbers to calculate the mean for.
    
    Returns:
        float: The mean of the list of numbers.
    """
    sum_of_array = sum(array)
    n_array = len(array)
    mean_value = sum_of_array / n_array
    return mean_value

def var(array):
    """
    Calculate the variance of a list of numbers.
    
    Parameters:
        array (list): The list of numbers to calculate the variance for.
    
    Returns:
        float: The variance of the list of numbers. Returns None if list has less than 2 elements.
    """
    mean_value = mean(array)
    n_array = len(array)
    if n_array < 2:
        return None

    deviation_sum = 0
    for value in array:
        deviation_sum += (value - mean_value) ** 2
    
    var_value = deviation_sum / (n_array - 1)
    return var_value

def std(array):
    """
    Calculate the standard deviation of a list of numbers.
    
    Parameters:
        array (list): The list of numbers to calculate the standard deviation for.
    
    Returns:
        float: The standard deviation of the list. Returns None if list has less than 2 elements.
    """
    if len(array) < 2:
        return None
    var_value = var(array)
    std_value = sqrt(var_value)
    return std_value

def median(array):
    """
    Calculate the median of a list of numbers.
    
    Parameters:
        array (list): The list of numbers to calculate the median for.
    
    Returns:
        float: The median of the list of numbers.
    """
    sort_array = sorted(array)
    n_array = len(sort_array)
    
    if n_array % 2 == 1:
        return sort_array[n_array // 2]
    else:
        median_below = sort_array[n_array // 2 - 1]
        median_upper = sort_array[n_array // 2]
        return (median_below + median_upper) / 2

def mode(array):
    """
    Calculate the mode(s) of a list of numbers.
    
    Parameters:
        array (list): The list of numbers to calculate the mode for.
    
    Returns:
        The mode of the list. Returns a list of modes if multiple modes are found.
    """
    frequencies = {}
    
    for value in array:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1
    
    max_freq = max(frequencies.values())
    modes = [value for value, frecuencia in frequencies.items() if frecuencia == max_freq]
    
    if len(modes) == 1:
        return modes[0]
    else:
        return modes[0]


start_time = time.time()

parser = argparse.ArgumentParser(
    prog='ComputeStatistics',
    description='Compute some statistics given a file with a list of numbers',
    epilog='Text at the bottom of help')

parser.add_argument('-f', '--file', type=str, required=True, help="file that contains numbers")

args = parser.parse_args()
file_name = args.file

array = open_file(file_name)
array = validate_type(array)

statistics = {"path": file_name,"len": 0, "mean": 0, "median": 0, "mode": 0, "std": 0, "var": 0}

if len(array) != 0:
    for f in [len,mean, median, mode, std, var]:
        statistics[f.__name__] = f(array)

end_time = time.time()

execute_time = end_time - start_time

print(f"Execute time: {execute_time} seg")
print("Results", statistics)
