from tkinter import *
from tkinter.ttk import *

import csv
from collections import namedtuple
import re

class SearchFrame(Tk):
    def __init__(self):
        self.inportData()
        self.aidedSearchPropts = [["refuge", "refuge"], ["Suicide\nPrevention" ,"at risk"], ["homeless","homeless"]]
        Tk.__init__(self, None)
        self.geometry("300x500")


        ###
        self.viewTabs = Notebook()
        self.viewTabs.place(x=50, y= 10)
        self.directSearchFrame = Frame(height=100, width=200)
        self.viewTabs.add(self.directSearchFrame, text="Direct Search")
        self.directSearchFeild = Entry(self.directSearchFrame)
        self.directSearchFeild.place(x=15, y=10)
        self.directSearchButton = Button(self.directSearchFrame, text="Search", command = self.directSearch)
        self.directSearchButton.place(x=15, y=40)
        self.assistedSearchFrame = Frame(height=200, width=200)
        self.buttonListing = Frame(self.assistedSearchFrame, height=100, width=150)
        self.buttonListing.place(x=5, y=30)
        self.checkBoxes = []
        for index in range(len(self.aidedSearchPropts)):
            cb = Checkbutton(self.buttonListing, text=self.aidedSearchPropts[index][0])
            cb.grid(row=index // 2, column = index % 2)
            self.aidedSearchPropts[index].append(cb)
        self.testLabel = Label(self.buttonListing, text="test data")
        self.radioSelection = IntVar()
        self.radioSelection.set(1)
        self.andRadioButton = Radiobutton(self.assistedSearchFrame, text="and", variable=self.radioSelection, value=1)
        self.andRadioButton.place(x=10, y=10)
        self.orRadioButton = Radiobutton(self.assistedSearchFrame, text="or", variable=self.radioSelection, value=2)
        self.orRadioButton.place(x=60, y=10)
        self.aidedSearchButton = Button(self.assistedSearchFrame, text="Search", command = self.indirectSearch)
        self.aidedSearchButton.place(x=50, y=140)
        self.viewTabs.add(self.assistedSearchFrame, text="Assisted Search")

        self.searchOutput = Listbox(self)
        self.searchOutput.place(x= 50, y=300)

    def directSearch(self):
        self.searchOutput.delete(0, END)
        inputText = self.directSearchFeild.get()
        for charity in self.charityDict.values():
            if re.search("disabled", charity.beneficiaries.lower(), re.IGNORECASE):
                print(charity.beneficiaries)
        count =0
        for index, content in self.charityDict.items():
            if re.fullmatch(inputText, index, re.IGNORECASE):
                #populate this combo box
                self.searchOutput.insert(count, content.name)
                count += 1

        for index, content in self.charityDict.items():
            if re.match(inputText, content.beneficiaries, re.IGNORECASE):
                #populate this combo box
                self.searchOutput.insert(count, content.name)
                count += 1
        for index, content in self.charityDict.items():
            if re.match(inputText, content.sector, re.IGNORECASE):
                #populate this combo box
                self.searchOutput.insert(count, content.name)
                count += 1


    def indirectSearch(self):
        self.searchOutput.delete(0, END)
        # NOTIMPLMENTED


    def inportData(self):
        self.charityDict = {}
        Charity = namedtuple('Charity', 'name website beneficiaries sector')
        file = open('data/char.csv')
        csvList = list(csv.reader(file, delimiter=','))
        for i, row in enumerate(csvList):
            if i == 0:
                # skip the first row as it is header data
                continue
            self.charityDict[row[1]] = Charity(row[0], row[3], row[42], row[39])

app = SearchFrame()
app.mainloop()