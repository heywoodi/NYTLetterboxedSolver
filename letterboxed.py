import json
import os
import time
import math
import itertools

LETTERS = ""

def get_dict():
    os.system("cls")
    with open("dict.json", "r") as read_file:
        data = json.load(read_file)
    dictionary = [i.upper() for i in data["words"]] #forcing words to be uppercase
    if LETTERS:
        valid = LETTERS
    else:
        input("What are todays letterboxd letters? ").upper()#userinput for todays puzzle
    os.system("cls")
    return dictionary, valid

def remove_invalid(dictionary, valid): #removing invalid words
    ALPHABET = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    invalid = [i for i in ALPHABET if i not in list(valid)] #collecting invalid letters
    dictionary = [i for i in dictionary if all(c not in i for c in invalid)]#removing words with invalid letters
    groups = [list(valid[:3]), list(valid[3:6]), list(valid[6:9]), list(valid[9:])]
    perms = []
    for n in range(len(groups)):
        perms = perms + list(itertools.permutations(groups[n], 2))#collecting invalid permutations of letters
    dictionary = [i for i in dictionary if all(a != b for a, b in zip(i, i[1:]))]#removing words with double letters
    dictionary = [i for i in dictionary if all((a,b) not in perms for a,b in zip(i, i[1:]))]#removing words with invalid permutations of letters
    return dictionary

def solve1(word, valid):#just a simple check that the word solves the puzzle in one
    must_contain = "".join([i for i in valid if i not in word])
    if not must_contain:#if must contain is empty return the word
        return (word)
    return None

def solve2(dictionary, word, valid):
    must_contain = "".join([i for i in valid if i not in word])#find the letters the second word must contain to solve
    remaining_words = [i for i in dictionary if i.startswith(word[-1])]#only condsider words that start with the last letter of the previous word
    for n in must_contain:
        remaining_words = [i for i in remaining_words if n in i]#remove words if they dont have a letter that it must contain
    if remaining_words:
        return (word, remaining_words)#return the valid answer if there is one!
    return None

def main():
    dictionary, valid = get_dict()#get dictionary from file
    t1 = time.time()#start timer
    dictionary = remove_invalid(dictionary, valid)#reduce dictionary
    results = []
    for word in dictionary:
        result = solve1(word, valid)#check if the word solves in one
        if not result:
            result = solve2(dictionary, word, valid)#check if the word can solve in two
            if result:
                for n in result[1]:
                    results.append((word, n))#collect solve in 2 results
        else:
            results.append(result)#collect solve in 1 results
    t2 = time.time()#end timer
    results.sort(key = lambda x:len(x[0]+x[1]), reverse=True)#sort answers based on least letters used
    for n in results:
        if len(n)==2:
            print(n[0], "and", n[1])#print the 2 solves
        else:
            print(n)#print the 1 solves
    print("time = " + str(math.floor((t2-t1)*1000)) + "ms")#print the timer

if __name__ == "__main__":
    main()