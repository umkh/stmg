import csv
import math
from datetime import date, datetime, timedelta

class Student:
    fields = ['StudentID', 'Name', 'Gender', 'Age', 'Enroll date', 'Midterm', 'Final', 'GPA']
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
        self._lastId()
    
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
        self.enroll_date = date.today().strftime("%Y/%m/%d")
        self.calculateGPA(self.midterm, self.final)
        new_record = {
            "StudentID": self.id,
            "Name": self.name,
            "Gender": self.gender,
            "Age": self.age,
            "Enroll date": self.enroll_date,
            "Midterm": float(self.midterm),
            "Final": float(self.final),
            "GPA": self.gpa
        }
        self.new_datas.append(new_record)
        self.id = self.id + 1

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
    
    def _openFile(self, file):
        self.id = 1
        self.file = file
        with open(self.file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')
            for row in reader:
                self.data.append(dict(row))

    def _lastId(self):
        if len(self.data) > 0:
            current_ID = self.data[-1].get("StudentID")
            self.id = int(current_ID) + 1

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
        if self.midterm != "":
            update["Midterm"] = float(self.midterm)
            self.calculateGPA(self.midterm, item["Final"])
        if self.final != "":
            update["Final"] = float(self.final)
            self.calculateGPA(item["Midterm"], self.final)
        