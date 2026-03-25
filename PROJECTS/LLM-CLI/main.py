import os
import requests
from colorama import Fore  #|Terminal Art Color|
import time
import json
from utils import print_ascii_art, ascii_art, ascii_text #|Terminal Art|
from keys import save_key, read_keys, erase_key, listen_keys, get_key

ais = {
"1" : "deepseek",
"2" : "chatgpt",
"3" : "gemini",
}

def crud_menu():
    while True:
        print("\n--- Gerenciar Chaves ---")
        print("1 - Save Keys")
        print("2 - Read Keys")
        print("3 - Erase Keys")
        print("4 - Listen Keys")
        print("5 - Return")
        option = input("Choose: ")
        if option == "1":
            name = input("AI Name")
            value = input("Key")
            save_key(name, value)
        elif option == "2":
            name = input("AI Name")           
            print(read_keys(name))
        elif option == "3":
            erase_key(name)
        elif option == "4":
            print(listen_keys())
        elif option == "5":
            break

def menu_prompt():
    ais = listen_keys()
    if not ais:
        print("No Keys")
        return
    print("Ais Online: ", ais)    
    name_ai = input("Choose a AI")
    key = listen_keys(name_ai)
    if not key:
        print("Keys dont Founded: ")
        return
    print(f"Using {name_ai}.")
    while True:
        command = input(f"{name_ai} >")
        if command.strip() == "--CLI CLose":
            break

       
if __name__ == "__main__":
    print_ascii_art(Fore.CYAN + ascii_art)
    print_ascii_art(Fore.LIGHTBLUE_EX + ascii_text)

while True:
    print("\n--- MAIN MENU ---")
    print("1 - Manage Keys")
    print("2 - Use AI Prompts")
    print("3 - Exit")
    option = input("Choose: ")
    if option == "1":
        crud_menu()
    elif option == "2":
        menu_prompt()
    elif option == "3":
        break 


    
# while True:
#     option = input("Choose a Option\n1-Keys, \n2-Writing Command, \n3-Close:\n")
#     try:
#         if option == '1':
#             option_key = input("Choose Key Option, \n1 = Save Key, \n2 = Read Key, \n3 = Erase Key, \n4 = Return: ")
#             if option_key == '1':
#                 key_name = input(cli_color + "Put Your Key Name 3-Cancel \nKey Name:")
#                 value = input(cli_color + "Put Key Value: ")
#                 save_key(key_name, value)
#             elif option_key == '2':
#                 reading_key()
#             elif option_key == '3':
#                 key_erase = input("Put The Key Which You Wanna Erase:")
#                 erase_key(key_erase)
#             else:
#                  continue
            
#         elif option == '2':
            
#             prompt = input("Writing Your Prompt")    

#         elif option == '3':
#             break

#     except Exception as e:
#         print("Error", e)

# print("GoodBye ^^")

if __name__ == "__main__":
    print_ascii_art(Fore.CYAN + ascii_art)
    print_ascii_art(Fore.LIGHTBLUE_EX + ascii_text)

    