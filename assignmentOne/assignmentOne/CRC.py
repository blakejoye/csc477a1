def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler='0'):


    polynomial_bitstring = polynomial_bitstring.lstrip('0')

    len_input = len(input_bitstring)

    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)

    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]

def main():
    input_bitstring = input("Enter the input binary sequence: ")
    polynomial_bitstring = input("Enter the polynomial bitstring (e.g., '1011'): ")

    if not all(c in '01' for c in input_bitstring) or not all(c in '01' for c in polynomial_bitstring):
        print("Invalid input! Only binary digits (0 or 1) are allowed.")
    else:
        remainder = crc_remainder(input_bitstring, polynomial_bitstring)
        print(f"CRC remainder for input {input_bitstring} using polynomial {polynomial_bitstring} is: {remainder}")

if __name__ == '__main__':
    main()
