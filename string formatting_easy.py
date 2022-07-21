def print_formatted(number):
    max_length_binary = len(str(bin(number).replace("0b", "")))
    def decimal(num):
        dec = str(num)
        decimal = " " * (max_length_binary - len(dec)) + dec
        return decimal
    def octal(num):
        dec_to_octal = str(oct(i).replace("0o", ""))
        octal = " " * (max_length_binary - len(dec_to_octal)) + dec_to_octal
        return octal
    def hexadecimal(num):
        dec_to_hexadecimal = str(hex(i).replace("0x", "")).capitalize()
        hexadecimal = " " * (max_length_binary - len(dec_to_hexadecimal)) + dec_to_hexadecimal
        return hexadecimal
    def binary(num):
        dec_to_binary = str(bin(i).replace("0b", ""))
        binary = " " * (max_length_binary - len(dec_to_binary)) + dec_to_binary
        return binary
    for i in range(1, number+1):       
        print(decimal(i), octal(i), hexadecimal(i), binary(i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)