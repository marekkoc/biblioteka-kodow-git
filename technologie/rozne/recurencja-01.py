"""

Rekurencja

Na podstawie: Tylor's Software - How to use recurention in Python

Created: 2024.11.11
Modified: 2024.11.11
"""
import os

def rec_to_up(my_path):    
    if my_path != os.sep:    
        print(os.getcwd())    
        my_head = os.path.split(my_path)[0]
        os.chdir(my_head)
        
        rec_to_up(my_head)        
    else:
        print("Recursion stopped...")
        return


if __name__ == "__main__":
    
    print()
    os.chdir('Desktop')
    full_path = os.getcwd()
    #print(os.getcwd())
    #folders = [f for f in os.listdir() if os.path.isdir(f)]
    
    rec_to_up(full_path)

    print()

