#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # Print basic message
    print("Hello, World!")
    
    # Ask for user input
    print("\nWanna do something? (1-Yes, 2-No)")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Great! Doing something...")
    elif choice == '2':
        print("Okay, doing nothing!")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

#PlaceHolder - AI