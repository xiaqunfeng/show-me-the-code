# -*- coding: utf-8 -*-

def filter_word(filename):
    f = open(filename, 'r')
    words = [line.strip() for line in f]

    while(True):
        s = input('please input your word: \n')
        if s == 'exit':
            break
        
        print('the result is: ')
        for word in words:
            if word in s:
                s = s.replace(word, '*'*len(word))
        print(s)

if __name__ == '__main__':
    filter_word('filtered_words.txt')
