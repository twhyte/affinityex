### Question generator for regionalism experiment
### Jan 1 2014
### tanya.whyte@mail.utoronto.ca


import csv
import os
import random
import itertools

# init object with lists for all key variables, including a G number system

class question(object):
    def __init__(self):

        #self.genderList = ["woman ", "man "]
        #self.genderNames = ["F", "M"]

        self.regionList = ["a Western province (British Columbia or Alberta)", "a prairie province (either Saskatchewan or Manitoba)", "Ontario", "the province of Quebec", \
                            "an Atlantic province (such as Nova Scotia or Newfoundland)"]
        self.regionNames = ["WEST", "PR", "ON", "QC", "ATL"]
        
        self.urbanList = ["lives in a rural area of ", "lives in a city in "]
        self.urbanNames = ["rural", "urban"]

        self.statusList = ["Aboriginal ", "immigrant ", "citizen who was born in Canada and "]
        self.statusNames = ["abo", "imm", "can"]

        self.incomeList = ["whose income is above the Canadian national average.", "whose income is below the Canadian national average."]
        self.incomeNames = ["high", "low"]

        self.languageList = ["an English-speaking ", "a French-speaking "]
        self.languageNames = ["english", "french"]

        self.IDNum = []

        self.sumOut = []
        self.textOut = []
        

    def permute(self):
        '''Writes questions of all permutations of tested variables. Placeholder:
        Myranthor: PLayer A lives in a rural region of the Province of Quebec.
        She is a French-speaking and  income is above the Canadian national average.'''
    

        initialScripts = ["This player "]
        workingScript = ""
        #permuteInternals = ["g", "r", "u", "s", "i", "l"]

        data={}

        idCounter = 1
        

        #for gender in self.genderList:
        for region in self.regionList:
            for urban in self.urbanList:
                for status in self.statusList:
                    for income in self.incomeList:
                        for language in self.languageList:
                            workingScript=""
                            pronoun="He "
                            possessive="His "
   
                            workingScript+=initialScripts[random.randrange(len(initialScripts))]+ urban + region+". "
                            workingScript+=pronoun+language+status+income

                            data[idCounter]=workingScript
                            self.IDNum.append(idCounter)
                            idCounter+=1

        return data

    def permuteBlocked(self):
        '''Writes questions of blocked permutations of tested variables.  The first three questions will be born-in-Canada.
        The fourth will be Aboriginal, and the fifth immigrant.
        Returns a dict of three lists: can, abo, imm
        Each list contains those permuted questions.'''
  
        initialScripts = ["This player "]
        workingScript = ""
        #permuteInternals = ["g", "r", "u", "s", "i", "l"]
    
        can = {}
        abo = {}
        imm = {}
        dataList = ["can", "abo", "imm"]
        
        data = dict(zip(dataList, [can, abo, imm]))

        idCounter = 1
        

        #for gender in self.genderList:
          
        for region in self.regionList:
            for urban in self.urbanList:
                for income in self.incomeList:
                    for language in self.languageList:

                        # three status containers need filling
                        # first three questions:
                        
                        workingScript=""
                        pronoun="He "
                        possessive="His "

                        workingScript+=initialScripts[random.randrange(len(initialScripts))]+ urban + region+". "
                        workingScript+=pronoun+language+"citizen who was born in Canada and "+income

                        data["can"][idCounter]=workingScript
                        self.IDNum.append(idCounter)
                        idCounter+=1

        print (idCounter)
        
        # aboriginal
        
        for region in self.regionList:
            for urban in self.urbanList:
                for income in self.incomeList:
                    for language in self.languageList:

                        
                        workingScript=""
                        pronoun="He "
                        possessive="His "

                        workingScript+=initialScripts[random.randrange(len(initialScripts))]+ urban + region+". "
                        workingScript+=pronoun+language+"Aboriginal "+income

                        data["abo"][idCounter]=workingScript
                        self.IDNum.append(idCounter)
                        idCounter+=1

        print (idCounter)

        # immigrant

        for region in self.regionList:
            for urban in self.urbanList:
                for income in self.incomeList:
                    for language in self.languageList:
                        
                        workingScript=""
                        pronoun="He "
                        possessive="His "

                        workingScript+=initialScripts[random.randrange(len(initialScripts))]+ urban + region+". "
                        workingScript+=pronoun+language+"immigrant "+income

                        data["imm"][idCounter]=workingScript
                        self.IDNum.append(idCounter)
                        idCounter+=1

        print (idCounter)

        return data

    def permuteBlockedNew(self): ## Urban Rural Block Test
        '''Writes questions of blocked permutations of tested variables.  The first three questions will be born-in-Canada.
        The fourth will be Aboriginal, and the fifth immigrant.
        Returns a dict of three lists: can, abo, imm
        Each list contains those permuted questions.'''
  
        initialScripts = ["This player "]
        workingScript = ""
        #permuteInternals = ["g", "r", "u", "s", "i", "l"]
    
        can = {}
        abo = {}
        imm = {}
        dataList = ["can", "abo", "imm"]
        
        data = dict(zip(dataList, [can, abo, imm]))

        idCounter = 1
        

        #for gender in self.genderList:

        # normal Canada
          
        for region in self.regionList:
            #for urban in self.urbanList:
            for income in self.incomeList:
                for language in self.languageList:

                    # three status containers need filling
                    # first three questions:
                    
                    workingScript=""
                    pronoun="She "
                    possessive="Her "

                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                    workingScript+=pronoun+language+"citizen who was born in Canada and "+income

                    data["can"][idCounter]=workingScript
                    self.IDNum.append(idCounter)
                    idCounter+=1

        print (idCounter)

        # urban/rural block

        for region in self.regionList:
            for urban in self.urbanList:
                for income in self.incomeList:
                    for language in self.languageList:

                        # three status containers need filling
                        # first three questions:
                        
                        workingScript=""
                        pronoun="She "
                        possessive="Her "

                        workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                        workingScript+=pronoun+language+"citizen who was born in Canada and "+income

                        data["can"][idCounter]=workingScript
                        self.IDNum.append(idCounter)
                        idCounter+=1

        
        print (idCounter)
        
        # aboriginal
        
        for region in self.regionList:
            #for urban in self.urbanList:
            for income in self.incomeList:
                for language in self.languageList:

                    
                    workingScript=""
                    pronoun="She "
                    possessive="Her "

                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                    workingScript+=pronoun+language+"Aboriginal "+income

                    data["abo"][idCounter]=workingScript
                    self.IDNum.append(idCounter)
                    idCounter+=1

        print (idCounter)

        # immigrant

        for region in self.regionList:
            #for urban in self.urbanList:
            for income in self.incomeList:
                for language in self.languageList:
                    
                    workingScript=""
                    pronoun="She "
                    possessive="Her "

                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                    workingScript+=pronoun+language+"immigrant "+income

                    data["imm"][idCounter]=workingScript
                    self.IDNum.append(idCounter)
                    idCounter+=1

        print (idCounter)

        return data


    def permuteBlockedURTest(self): ## Urban Rural Block Test
        '''Writes questions of blocked permutations of tested variables.  The first three questions will be born-in-Canada.
        The fourth will be Aboriginal, and the fifth immigrant.
        Returns a dict of three lists: can, abo, imm
        Each list contains those permuted questions.'''
  
        initialScripts = ["This player "]
        workingScript = ""
        #permuteInternals = ["g", "r", "u", "s", "i", "l"]
    
        can = {}
        abo = {}
        imm = {}
        dataList = ["can", "abo", "imm"]
        
        data = dict(zip(dataList, [can, abo, imm]))

        idCounter = 1
        

        #for gender in self.genderList:
          
        for region in self.regionList:
            #for urban in self.urbanList:
            for income in self.incomeList:
                for language in self.languageList:

                    # three status containers need filling
                    # first three questions:
                    
                    workingScript=""
                    pronoun="He "
                    possessive="His "

                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                    workingScript+=pronoun+language+"citizen who was born in Canada and "+income

                    data["can"][idCounter]=workingScript
                    self.IDNum.append(idCounter)
                    idCounter+=1

        print (idCounter)
        
        # aboriginal
        
        for region in self.regionList:
            #for urban in self.urbanList:
            for income in self.incomeList:
                for language in self.languageList:

                    
                    workingScript=""
                    pronoun="He "
                    possessive="His "

                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                    workingScript+=pronoun+language+"Aboriginal "+income

                    data["abo"][idCounter]=workingScript
                    self.IDNum.append(idCounter)
                    idCounter+=1

        print (idCounter)

        # immigrant

        for region in self.regionList:
            #for urban in self.urbanList:
            for income in self.incomeList:
                for language in self.languageList:
                    
                    workingScript=""
                    pronoun="He "
                    possessive="His "

                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
                    workingScript+=pronoun+language+"immigrant "+income

                    data["imm"][idCounter]=workingScript
                    self.IDNum.append(idCounter)
                    idCounter+=1

        print (idCounter)

        return data


# output summary guide to .csv and output text blocks to .txt
    def output(self, dataFile = "data.txt", summaryFile = "summary.csv", permuteFile = "permutations.csv"):
        '''Output'''

        data=self.permute()
        f = open(dataFile, 'w')
        s = open(summaryFile, 'w')
        p = open(permuteFile, 'w')
        
        writer = csv.writer(s, lineterminator='\n')
        writer.writerow(["qid", "region", "urban", "status", "income", "language"])
        varList = ["region", "urban", "status", "income", "language"]
        
        iterHolder = []
        
        for i in self.IDNum:
            tempText = data[i]
            # text file
            f.write("G"+str(i)+'\n')
            f.write(data[i]+'\n\n')

            # csv file
            tempRow = []
            tempRow.append("G"+str(i))
            iterHolder.append(("G"+str(i)))
            

            for r in self.regionList:
                if r in tempText:
                    tempRow.append(self.regionNames[self.regionList.index(r)])
            for u in self.urbanList:
                if u in tempText:
                    tempRow.append(self.urbanNames[self.urbanList.index(u)])
            for t in self.statusList:
                if t in tempText:
                    tempRow.append(self.statusNames[self.statusList.index(t)])
            for n in self.incomeList:
                if n in tempText:
                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
            for l in self.languageList:
                if l in tempText:
                    tempRow.append(self.languageNames[self.languageList.index(l)])
            writer.writerow(tempRow)

        x = list(itertools.islice(itertools.combinations(iterHolder, 2), 100000))

        # close properly
        f.close()
        s.close()

        return x

    def outputBlocked(self, dataFile = "dataBlocked.txt", summaryFile = "summaryBlocked.csv", permuteFile = "permutationsBlocked.csv"):
        '''Output'''

        data=self.permuteBlocked()
        f = open(dataFile, 'w')
        s = open(summaryFile, 'w')
        p = open(permuteFile, 'w')
        
        writer = csv.writer(s, lineterminator='\n')
        writer.writerow(["qid", "region", "urban", "status", "income", "language"])
        varList = ["region", "urban", "status", "income", "language"]
        
        iterHolder = []

        
        for i in self.IDNum:
            tempText = data[i]
            # text file
            f.write("G"+str(i)+'\n')
            f.write(data[i]+'\n\n')

            # csv file
            tempRow = []
            tempRow.append("G"+str(i))
            iterHolder.append(("G"+str(i)))
            

            for r in self.regionList:
                if r in tempText:
                    tempRow.append(self.regionNames[self.regionList.index(r)])
            for u in self.urbanList:
                if u in tempText:
                    tempRow.append(self.urbanNames[self.urbanList.index(u)])
            for t in self.statusList:
                if t in tempText:
                    tempRow.append(self.statusNames[self.statusList.index(t)])
            for n in self.incomeList:
                if n in tempText:
                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
            for l in self.languageList:
                if l in tempText:
                    tempRow.append(self.languageNames[self.languageList.index(l)])
            writer.writerow(tempRow)

        x = list(itertools.islice(itertools.combinations(iterHolder, 2), 100000))

        # close properly
        f.close()
        s.close()

        return x





