import argparse
import time
try:
    import pandas as pd
except ImportError:
    pd = None
    print("Pandas package not found")
    
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
        with open(file_name, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied when trying to read {file_name}.")
        return []
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")
        return []
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
        int(s)
        return True
    except ValueError:
        return False

def validate_type(array):
    """
    Convert a list of strings to int where possible, ignoring non-numeric values.
    
    Parameters:
        array (list): A list of strings to be validated and converted.
    
    Returns:
        list: A list of int converted from numeric strings in the original list.
    """
    array_numeric = []
    for value in array:
        if is_number(value):
            array_numeric.append(int(value))
        else:
            print(f"Value non numeric found {value} replace by None")
            array_numeric.append(None)

    return array_numeric

def output_file(result):
    """Create output text file

    Parameters
    ----------
    result : dictionary
        dictionary with result values of the file 
    """

    with open("ConvertionResults.txt","w") as f:
        f.write(str(result))

def int_to_bin(num, bits=8):
    """
    Converts an integer to its binary representation using two's complement for negative numbers.

    Parameters:
    - num (int): The integer to convert.
    - bits (int): The number of bits for the binary representation.

    Returns:
    - str: The binary representation of the integer using two's complement for negative numbers.
    """
    if num is None:
        return None
    
    if num >= 0:
        binary = ''
        if num == 0:
            binary = '0'
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
    else:
        num = abs(num)
        binary = ''
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2

        binary = binary.zfill(bits)

        binary_invert = ''.join('1' if b == '0' else '0' for b in binary)

        binary_complement = ''
        carry = 1
        for i in range(len(binary_invert) - 1, -1, -1):
            if binary_invert[i] == '1' and carry == 1:
                binary_complement = '0' + binary_complement
            elif binary_invert[i] == '0' and carry == 1:
                binary_complement = '1' + binary_complement
                carry = 0
            else:
                binary_complement = binary_invert[i] + binary_complement
        binary = binary_complement

    return binary.zfill(bits)

def bin_to_hex(bin_str):
    """
    Converts a binary string to its hexadecimal representation.

    Parameters:
    - bin_str (str): A string representing a binary number.

    Returns:
    - str: The hexadecimal representation of the given binary number.
    """
    if bin_str is None:
        return None
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    bin_str = bin_str.zfill(len(bin_str) + (4 - len(bin_str) % 4) % 4)
    for i in range(0, len(bin_str), 4):
        four_bits = bin_str[i:i+4]
        decimal = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(reversed(four_bits)))
        hexadecimal += hex_digits[decimal]
    return hexadecimal

def int_to_hex(num, bits=32):
    """
    Converts an integer to its hexadecimal representation using two's complement for negative numbers.

    Parameters:
    - num (int): The integer to convert.
    - bits (int): The number of bits for the binary representation before converting to hexadecimal.

    Returns:
    - str: The hexadecimal representation of the integer using two's complement for negative numbers.
    """
    if num is None:
        return None
    
    bin_str = int_to_bin(num, bits)

    return bin_to_hex(bin_str)


def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(description='Compute statistics from a file containing numbers.')
    parser.add_argument('-f', '--file', type=str, required=True, help="File that contains numbers")
    args = parser.parse_args()

    file_name = args.file
    array = open_file(file_name)
    array_numeric = validate_type(array)
    
    result = {"path": file_name, "n_array": len(array_numeric), "binary_array":[], "hex_array": [] }
    
    result["binary_array"] = list(map( int_to_bin, array_numeric,))
    result["hex_array"] = list(map( int_to_hex, array_numeric))
    if pd :
        data_result = pd.DataFrame()
        data_result["Number"] = array_numeric
        data_result["Path"] = file_name
        data_result["binary_array"] = result["binary_array"]
        data_result["hex_array"] = result["hex_array"]
        data_result.to_csv("./ConvertionResults.txt", sep = "\t", index = False)
        result = data_result.head(10)
    else:
        output_file(result)
    end_time = time.time()
    execute_time = end_time - start_time
    print("Filename: ", file_name)
    print(f"Execute time: {execute_time} seconds")
    print("Results:", result)

if __name__ == "__main__":
    main()