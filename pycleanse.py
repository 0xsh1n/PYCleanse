import re
import ast
import base64
import hashlib
from Crypto.Cipher import AES
from pystyle import *
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner_text = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢤⣄⡀⠀⠀⠀⠀⣠⡎⠀⣀⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣬⣿⣿⣶⣤⣰⣿⣧⣾⣿⣟⣤⣴⣖⣂⣀⣀⣀⣀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣵⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠉⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠶⠿⢿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠟⠁⠀⠀⠀⢀⠠⠐⠂⠉⠉⠉⠀⠒⠢⠀⡀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣽⣿⣿⣿⠏⠀⠀⢀⠔⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢦⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡟⠀⠀⢀⠜⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⣻⣿⣿⣿⡄⠻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠀⠀⢠⠂⠀⠀⠀⣠⠒⠊⠁⠀⠀⠈⠉⠒⢄⠀⠀⠀⠀⢱⠦⠀⠀⠀⢻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠃⠀⢀⠆⠀⠀⢠⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡳⡄⠀⠀⠀⢱⠀⠀⠀⢸⣿⣿⡿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣼⠟⣿⣿⡟⠀⠀⡌⠀⠀⡰⠃⠀⢀⡠⠒⠒⠒⠒⠢⣄⠀⠀⠀⠘⣄⠀⠀⠀⢧⠀⠀⠀⣿⣿⣧⠙⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⣿⣿⡇⠀⢰⠉⠀⢰⠁⠀⡰⠉⠀⠀⠀⠀⠀⠀⠀⠣⡀⠀⠀⠈⡆⠀⠀⠘⡄⠀⠀⢻⣿⡻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⣿⡇⠀⡘⠀⠀⡆⠀⡜⠀⣀⠤⠖⠒⠢⣄⠀⠀⠠⡵⡀⠀⠀⢰⠀⠀⠀⢃⠀⠀⢸⣿⡇⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢻⡇⠀⡇⠀⢸⠀⡘⢠⠞⠁⠀⠀⠀⠀⠈⢣⠀⠀⠈⢷⠀⠀⠀⠆⠀⠀⠸⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠗⠀⠸⢠⠱⢃⡠⠤⠠⢤⣀⠀⠀⢀⡇⠀⠀⠘⡀⠀⠀⡇⠀⠀⠀⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⢱⠀⢸⣌⣵⣷⣦⣄⠀⠀⠘⡆⠀⠸⢅⠀⠀⠀⡇⠀⠀⡇⠀⠀⢀⠀⠠⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢦⠸⣿⣿⣿⣿⣿⡧⠀⠀⡍⠄⠀⠘⠀⠀⠀⠇⠀⠀⠇⠀⠀⢸⠁⠈⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠈⢢⡹⣿⡿⣿⠿⠳⠀⢸⡗⠀⠀⡇⠀⠀⢰⠆⠀⢸⠄⠀⠀⠸⠀⠀⢸⣿⠓⠒⠂⠤⠤⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣶⣦⣬⣉⠉⢀⠔⠁⠀⡟⠀⠀⠴⠁⠀⢀⠏⠀⠀⡎⠀⢀⡰⡇⠀⢐⣿⣿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠐⠂⠤⢀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠒⠈⠁⠘⣿⣆⠉⠛⠒⠈⠀⠀⣀⠞⠀⢀⠔⠁⠀⣺⠏⠀⡠⡲⠀⠀⢞⠵⠂⠐⣵⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣱⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡀⠔⠊⠁⠀⠀⠀⠀⠀⠀⠸⣿⡿⠿⠷⠾⠞⠊⢀⣰⠶⠃⠀⠀⢘⠏⢀⡲⠽⠃⢀⠠⣫⠃⢀⢔⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣒⣂⣠⣔⠺⠓⠁⠀⣀⣐⠜⠁⠀⢤⡐⠁⠈⢕⠝⡍⢀⠰⣱⣿⣰⢦⢄⡀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢱⣬⣤⣀⣀⡴⣾⢳⠟⠁⠀⢈⢙⣊⢠⡐⣌⠔⡞⢐⢦⢪⣿⣿⡥⡎⣞⣼⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢢⠃⢻⡍⢠⠉⠉⠉⠓⠀⢠⣬⡝⢩⡄⣥⠂⣴⡟⣴⢹⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠀⠀
⠀⠀⠀⠀⢸⣶⣤⣄⣀⠀⠀⠀⠀⠀⡠⡠⣪⡪⡫⣺⢣⢫⣿⣽⣟⠓⣼⣟⠫⣐⡓⢚⠻⢅⣚⣿⣾⣶⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣶⣦⣤⣎⣾⡫⣪⢞⠕⣡⣿⣼⣿⣮⣩⣂⣶⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡀⢀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    '''
    print(Center.XCenter(Colors.red + banner_text))
    print(Center.XCenter(Colors.red + "               ~> PYCleanse <~"))
    print(Center.XCenter(Colors.red + "               ~~> Made by 0xsh1n <~~\n\n"))

def get_input_filename():
    while True:
        text = "File name: "
        filename = input(Colorate.Color(Colors.red, text, True))
        if os.path.exists(filename):
            return filename
        else:
            print(Colorate.Color(Colors.red, "Error: File does not exist. Please enter a valid filename.", True))
            
        
            
def derive_key_and_iv(password, salt):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    key, iv = dk[:16], dk[16:]
    return key, iv

def decrypt_aes_data(encrypted_data, key):
    encrypted_data = base64.b85decode(encrypted_data)
    salt, key, iv = encrypted_data[:8], *derive_key_and_iv(key, encrypted_data[:8])
    cipher = AES.new(key, AES.MODE_CFB, iv)
    data = cipher.decrypt(encrypted_data[8:])
    return data.decode()

def read_lines_from_file(file_path):
    with open(file_path, "r") as file_handle:
        return file_handle.readlines()

def find_and_extend_obfuscated_data(lines, obfuscate_str, line_number):
    while line_number < len(lines):
        line = lines[line_number].strip()

        # Check if the line is part of the obfuscated data
        if ".replace('\\n','')]))" in obfuscate_str:
            break

        # Skip empty lines or lines starting with a comment
        if not line or line.startswith("#"):
            line_number += 1
            continue

        obfuscate_str += lines[line_number]
        line_number += 1

        # Check if deobfuscation is complete
        if ".replace('\\n','')]))" in obfuscate_str:
            break

    return obfuscate_str, line_number
    


def locate_obfuscated_data(lines):
    for i, line in enumerate(lines, start=1):
        match = re.search(r'obfuscate = (.+)', line)
        if match:
            return match.group(1), i
    return "", -1


def main():
    clear_screen()
    print_banner()

    input_filename = get_input_filename()
    lines = read_lines_from_file(input_filename)

    obfuscate_str, line_number = locate_obfuscated_data(lines)

    if not obfuscate_str:
        print(Colorate.Color(Colors.red, "Error: The file does not appear to be obfuscated with pyobfuscate.com", True))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

    if ".replace('\\n','')]))" not in obfuscate_str:
        obfuscate_str, line_number = find_and_extend_obfuscated_data(lines, obfuscate_str, line_number)
        
    comment = "# deobfuscated by 0xsh1n\n\n"

    obfuscate_data = str(eval(obfuscate_str))
    obfuscate_dict = ast.literal_eval(obfuscate_data)

    encrypted_data, encryption_key = list(obfuscate_dict.values())[0], list(obfuscate_dict.keys())[0][1:-1]

    original_filename = input_filename.split('.')[0]  # Extracting the original file name without extension
    output_filename = f"{original_filename}_deobfuscated.py"  # Combining with the deobfuscated suffix

    with open(output_filename, "w", encoding="utf-8") as output_handle:
        output_handle.write(comment + decrypt_aes_data(encrypted_data, encryption_key))
        print(Colorate.Color(Colors.red, "Your file has been deobfuscated successfully, source code is now in {}!\n".format(output_filename), True))
        return

# ... (other code remains unchanged)

if __name__ == "__main__":
    main()
