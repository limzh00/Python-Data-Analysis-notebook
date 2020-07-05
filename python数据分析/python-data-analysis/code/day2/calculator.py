#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Minzhang Li
# FILE: C:\Users\Administrator\Desktop\python数据分析\python基础语法以及配套
# 练习(持续更新)-lmz\basic\day2\calculator.py
# DATE: 2020/07/05 Sun
# TIME: 07:56:30

# DESCRIPTION: This is a simple calculator to test your acknowledgement of basic operation on integers and floating number

# ######################################### YOU SHOULD REPLACE `pass` WITH YOUR CODES #######################################
def main():
    print("Please choose mode with its number : \n 1. addition \t 2.substraction \t 3.multiplication \t 4.division")
    # Code 1: Catch the input
    print("Plase enter two numbers splitted by a space")
    x ,y = map(int, input().split())
    result = 0
    if(n == '1'):
        pass # Code 2
        result = x + y
    elif(n == '2'):
        pass # Code 3
        result = x - y
    elif(n == '3'):
        pass # Code 4
    elif(n == '4'):
        pass # Code 5
    else:
        print('Invalid input.')
        return 
    print("The result is: ")
    # Code 6: output the result

if __name__ == '__main__':
    main()