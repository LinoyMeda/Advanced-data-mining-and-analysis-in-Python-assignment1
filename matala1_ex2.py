# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:52:26 2023
matala1
@author: Linoy Medalsy
"""

#ex2

def revword(word:str):
    fixedW = word.lower()[::-1]
    return fixedW


def countword():
    #str_file1 = open("text.txt", 'r')
    str_file = open("C:\\Users\\linoy\\OneDrive\\שולחן העבודה\\לימודים\\תואר\\שנה ג\\סמסטר ב\\כרייה וניתוח נתונים מתקדם בפייתון\\קודים\\מטלות\\text.txt", 'r')
    for line in str_file:
        row = line.split()
        if len(row) == 1:
            word = row[0].lower().strip()
            counter = 1
        else:
            for w in row:
                elm = revword(w)
                if elm == word:
                    counter +=1
    return counter

print(countword())


#"C:\\Users\\linoy\\OneDrive\\שולחן העבודה\\לימודים\\תואר\\שנה ג\\סמסטר ב\\כרייה וניתוח נתונים מתקדם בפייתון\\קודים\\מטלות\\text.txt"