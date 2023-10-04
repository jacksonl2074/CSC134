# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:17:12 2023

@author: lkjac

Program asks user to input highest temperature for each month of the year
then program calculates the average temp and displays highest and lowest temps.
10.4.23
CSC 121 M3HW3 - Lists
Laura K. Jackson
"""


def main():
    '''
    This is the main function. Asks for user to enter highest temp's for each
    month of the year. Afterwards, the average temp is calculated and displayed,
    and the highest and lowest temps are displayed.
    
    Returns
    -------
    None.

    '''
    print("hello bubbles")

    # create an empty list
    tempsList = []
    janTemp = float(
        input("Please enter the highest recorded temperature for January: "))
    febTemp = float(
        input("Please enter the highest recorded temperature for February: "))
    marTemp = float(
        input("Please enter the highest recorded temperature for March: "))
    aprTemp = float(
        input("Please enter the highest recorded temperature for April: "))
    mayTemp = float(
        input("Please enter the highest recorded temperature for May: "))
    junTemp = float(input("Please enter the highest recorded temperature for June: "))
    julTemp = float(input("Please enter the highest recorded temperature for July: "))
    augTemp = float(input("Please enter the highest recorded temperature for August: "))
    sepTemp = float(input("Please enter the highest recorded temperature for September: "))
    octTemp = float(input("Please enter the highest recorded temperature for October: "))
    novTemp = float(input("Please enter the highest recorded temperature for November: "))
    decTemp = float(input("Please enter the highest recorded temperature for December: "))
    
    tempsList = [janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, 
                 augTemp, sepTemp, octTemp, novTemp, decTemp]
    
   
    
    # print(tempsList)
    print("Fayetteville, NC 2022 Temp\n")
    print("--------------------------\n")
    
    
    matrix = [['January', janTemp], ['February', febTemp], ['March', marTemp],
              ['April', aprTemp], ['May', mayTemp], ['June', junTemp],
              ['July', julTemp], ['August', augTemp], ['September', sepTemp],
              ['October', octTemp], ['November', novTemp], ['December',
                                                            decTemp]]
    # print info as a table
    # use f-string to format table FIXME!
    for row in matrix:
        for cell in row:
            print(cell, end='\t\t')
        print()
        
    print("--------------------------\n")
    
    # use min and max methods to print out lowest/highest temps
    highTemp = max(tempsList)
    lowestTemp = min(tempsList)
    
    # average usig sum and len methods
    avgTemp = sum(tempsList)/ len(tempsList)
    
    print("Highest Temp: ", highTemp)
    print("Lowest Temp: ", lowestTemp)
    print("Average temp: ", avgTemp)
    

if __name__ == "__main__":
    main()
