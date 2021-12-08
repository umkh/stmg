import csv
import math
from datetime import date, datetime, timedelta

class Student:
    fields = ['StudentID', 'Name', 'Gender', 'Age', 'Enrollment date', 'Midterm', 'Final', 'GPA']
    data = []
    new_datas = []
    file = object

    id = 0
    name = ""
    gender = 0
    age = 0
    enroll_date = ""
    midterm = 0
    final = 0
    gpa = 0

    def __init__(self, file):
        self._openFile(file)
    
    def calculateGPA(self, midterm, final):
        self.gpa = math.ceil(0.4*float(midterm)+0.6*float(final))
    
    def calculate_grad_date(self, enroll_date: str, duration: str) -> str:
        args = duration.split(' ')
        weeks = ((int(args[0])*12)+(int(args[1])))*4.35
        enroll_date = datetime.strptime(enroll_date, "%Y/%m/%d")
        end_date = enroll_date + timedelta(weeks=weeks)
        return end_date.strftime("%Y/%m/%d")

    def printAll(self):
        for item in self.fields:
            print("%-15s"%item, end='')
        print("\n")
        for row in self.data:
            for key, val in row.items():
                print("%-15s"%val, end='')
            print("\n")
        for row in self.new_datas:
            for key, val in row.items():
                print("%-15s"%val, end='')
            print("\n")

    def getStudent(self, id) -> object:
        for item in self.data:
            if item["StudentID"] == id:
                self.id = id
                return item
        return ""

    def add(self):
        self.calculateGPA(self.midterm, self.final)
        new_record = {
            "StudentID": self.id,
            "Name": self.name,
            "Gender": self.gender,
            "Age": self.age,
            "Enrollment date": self.enroll_date,
            "Midterm": float(self.midterm),
            "Final": float(self.final),
            "GPA": self.gpa
        }
        self.new_datas.append(new_record)

    def update(self, id):
        update = {}

        for item in self.data:
            if item["StudentID"] == id:
                self._validate(item, update)
                item.update(update)        
        
        self._save()

    def save_to_disk(self):
        if len(self.new_datas) > 0:
            self._save()
            self.new_datas = []
    
    def _openFile(self, file):
        self.id = 1
        self.file = file
        with open(self.file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')
            for row in reader:
                self.data.append(dict(row))

    def _save(self):
        with open(self.file, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=self.fields)
            writer.writeheader()
            for item in self.new_datas:
                self.data.append(item)
            for w in self.data:
                writer.writerow(w)

    def _validate(self, item, update):
        if self.name != "":
            update["Name"] = self.name
        if self.gender != "":
            update["Gender"] = self.gender
        if self.age != "":
            update["Age"] = self.age
        if self.enroll_date != "":
            update["Enrollment date"] = self.enroll_date
            
        if self.midterm != "":
            update["Midterm"] = float(self.midterm)
        else:
            self.midterm = item["Midterm"]
        if self.final != "":
            update["Final"] = float(self.final)
        else:
            self.final = item["Final"]


        self.calculateGPA(self.midterm, self.final)
        update["GPA"] = float(self.gpa)
        