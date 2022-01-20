import os
from requests import get
import json
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self):
        self.response = get('http://db.cs.pitt.edu/courses/cs1656/data/hours.json', verify=False) 
        self.hours = json.loads(self.response.content) 

    def part4(self):
        #write output to hours.csv

    def part5(self):
        #write output to 'part5.txt'
        f = open('part5.txt', 'w') 

    def part6(self):
        #write output to 'part6.txt'
        f = open('part6.txt', 'w') 

    def part7(self):
        #write output to 'part7.txt'
        f = open('part7.txt', 'w') 
        

if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()