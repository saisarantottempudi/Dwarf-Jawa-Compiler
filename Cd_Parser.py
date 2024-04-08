from ourrules import Consts
import sys
import os


# Lexical Analyser
def lexical_analyser():
    keywords = ['unit', 'main', 'begin', 'for', 'to', 'do', 'if', 'endif', 'endfor', 'return', 'End']
    operators = ['(', ')', '[', ']', '=', '-', '>']
    w = ""

    if os.stat("/Users/padmavathikadium/Desktop/question").st_size == 0:
        print("File is empty")
    else:
        with open('/Users/padmavathikadium/Desktop/question', 'r') as f:
            for line in f:
                for word in line:
                    for character in word:
                        if character.isspace() or character == ';':
                            if w == "":
                                continue
                            elif w in keywords:
                                print("%s : Keyword" % w)
                            else:
                                print("%s : Identifier" % w)
                            w = ""
                        elif character in operators:
                            print("%s : Operator" % character)
                            if w == "":
                                continue
                            elif w in keywords:
                                print("%s : Keyword" % w)
                            else:
                                print("%s : Identifier" % w)
                            w = ""
                        else:
                            w = w + character


# Tokenizer
def tokenizer(program_string):
    tokens = Consts.tokens
    ip = 0
    program_string += '$'
    token_string = ""
    while program_string[ip] != '$':
        current_token = ""
        if program_string[ip].isalpha() or program_string[ip] == '_':
            current_token += program_string[ip]
            ip += 1
            while program_string[ip].isalnum() or program_string[ip] == '_':
                current_token += program_string[ip]
                ip += 1
            if current_token in tokens.keys():
                token_string += tokens[current_token]
            else:
                token_string += tokens['var']
        elif program_string[ip].isnumeric():
            current_token += program_string[ip]
            ip += 1
            while program_string[ip].isnumeric() or program_string[ip] == '.':
                current_token += program_string[ip]
                ip += 1
            token_string += tokens['num']
        else:
            if program_string[ip] in tokens:
                token_string += tokens[program_string[ip]]
                ip += 1
            else:
                nl_count = 1
                pointer_count = 0
                for _ in range(ip):
                    if program_string[_] == '\n':
                        nl_count += 1
                        pointer_count = 0
                    else:
                        pointer_count += 1
                print("Tokenizer: Error on line " + str(nl_count) + " on column " + str(pointer_count))

                exit()
    return token_string


# # Main function
def main():
    file = open("/Users/padmavathikadium/Desktop/question", "r")
    program_string = file.read()
    print("\nProgram:\n")
    print(program_string)
    print("\nLexical Analysis:\n")
    lexical_analyser()
    print("\nTokens Generated:")
    # Tokenizing
    token_string = tokenizer(program_string)
    print(token_string)


main()

