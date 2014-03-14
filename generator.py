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

        self.playerList = ["Player A lives in", "Player B lives in"]
        self.playerNames = ["A", "B"]
        self.regionList = [' a western province(<span style="color:black;font-size:medium;cursor:help;" title="Includes British Columbia and Alberta.">&#9733</span>)', \
                           ' a prairie province(<span style="color:black;font-size:medium;cursor:help;" title="Includes Saskatchewan and Manitoba.">&#9733</span>)', \
                           ' Ontario(<span style="color:black;font-size:medium;cursor:help;" title="The Province of Ontario.">&#9733</span>)', \
                           ' the province of Quebec(<span style="color:black;font-size:medium;cursor:help;" title="The Province of Quebec.">&#9733</span>)', \
                        ' an Atlantic province(<span style="color:black;font-size:medium;cursor:help;" title="Includes Newfoundland and Labrador, Nova Scotia, New Brunswick, and Prince Edward Island.">&#9733</span>)']
        self.regionNames = ["WEST", "PR", "ON", "QC", "ATL"]
        
        self.urbanList = [" a rural area of", " a city in"]
        self.urbanNames = ["rural", "urban"]

##        self.statusList = ["Aboriginal ", "immigrant ", "citizen who was born in Canada and "]
##        self.statusNames = ["abo", "imm", "can"]

        self.incomeList = ["whose income is above the Canadian national average.", "whose income is below the Canadian national average."]
        self.incomeNames = ["high", "low"]

        self.languageList = ["is an anglophone ", "is a francophone "]
        self.languageNames = ["english", "french"]

        self.IDNum = []

        self.sumOut = []
        self.textOut = []

        self.questionHTML = '<table style="width: 500px;table-layout: fixed;" border="3" cellpadding="2" cellspacing="2"><tbody><tr><td cstyle="text-align: center;" style="text-align: center;" bgcolor="#a3d39"><br><strong>Player A</strong><br>&nbsp;</td><td style="text-align: center;" bgcolor="#6dcff6"><strong>Player B</strong></td></tr><tr><td><div style="text-align: center;"><br>&nbsp;PLACEHOLDERA<br>&nbsp;</div></td><td style="text-align: center;"><br>&nbsp;PLACEHOLDERB<br>&nbsp;</td></tr></tbody></table><br>&nbsp;<br><strong><em>How would you allocate winnings between these two participants?<br>The total must equal $49.</em></strong>'

        
    def permute(self):
        '''Writes questions of all permutations of tested variables. Placeholder: QQQ'''
    

        initialScripts = ["QQQ lives in"]
        workingScript = ""
        #permuteInternals = ["g", "r", "u", "s", "i", "l"]

        data={}

        idCounter = 1
        

        #for gender in self.genderList:
        for region in self.regionList:
            for urban in self.urbanList:
                #for status in self.statusList:
                for income in self.incomeList:
                    for language in self.languageList:
                        workingScript=""
##                        pronoun="He "
##                        possessive="His "

                        workingScript+=initialScripts[random.randrange(len(initialScripts))]+ urban + region+". "
                        workingScript+="<br>&nbsp;<br>The player "+language+income

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
        rur = {}
        abo = {}
        imm = {}
        dataList = ["can", "rur", "abo", "imm"]
        
        data = dict(zip(dataList, [can, rur, abo, imm]))

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

                        workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + urban + region+". "
                        workingScript+=pronoun+language+"citizen who was born in Canada and "+income

                        data["rur"][idCounter]=workingScript
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



##    def permuteBlockedURTest(self): ## Urban Rural Block Test
##        '''Writes questions of blocked permutations of tested variables.  The first three questions will be born-in-Canada.
##        The fourth will be Aboriginal, and the fifth immigrant.
##        Returns a dict of three lists: can, abo, imm
##        Each list contains those permuted questions.'''
##  
##        initialScripts = ["This player "]
##        workingScript = ""
##        #permuteInternals = ["g", "r", "u", "s", "i", "l"]
##    
##        can = {}
##        abo = {}
##        imm = {}
##        dataList = ["can", "abo", "imm"]
##        
##        data = dict(zip(dataList, [can, abo, imm]))
##
##        idCounter = 1
##        
##
##        #for gender in self.genderList:
##          
##        for region in self.regionList:
##            #for urban in self.urbanList:
##            for income in self.incomeList:
##                for language in self.languageList:
##
##                    # three status containers need filling
##                    # first three questions:
##                    
##                    workingScript=""
##                    pronoun="He "
##                    possessive="His "
##
##                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
##                    workingScript+=pronoun+language+"citizen who was born in Canada and "+income
##
##                    data["can"][idCounter]=workingScript
##                    self.IDNum.append(idCounter)
##                    idCounter+=1
##
##        print (idCounter)
##        
##        # aboriginal
##        
##        for region in self.regionList:
##            #for urban in self.urbanList:
##            for income in self.incomeList:
##                for language in self.languageList:
##
##                    
##                    workingScript=""
##                    pronoun="He "
##                    possessive="His "
##
##                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
##                    workingScript+=pronoun+language+"Aboriginal "+income
##
##                    data["abo"][idCounter]=workingScript
##                    self.IDNum.append(idCounter)
##                    idCounter+=1
##
##        print (idCounter)
##
##        # immigrant
##
##        for region in self.regionList:
##            #for urban in self.urbanList:
##            for income in self.incomeList:
##                for language in self.languageList:
##                    
##                    workingScript=""
##                    pronoun="He "
##                    possessive="His "
##
##                    workingScript+=initialScripts[random.randrange(len(initialScripts))]+ "lives in" + region+". "
##                    workingScript+=pronoun+language+"immigrant "+income
##
##                    data["imm"][idCounter]=workingScript
##                    self.IDNum.append(idCounter)
##                    idCounter+=1
##
##        print (idCounter)
##
##        return data


# output summary guide to .csv and output text blocks to .txt
    def output(self, dataFile = "data.txt", summaryFile = "summary.csv"):
        '''Output'''

        data=self.permute()
        f = open(dataFile, 'w')
        s = open(summaryFile, 'w')
        
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

    def outputBlocked(self, dataFile = "dataBlocked.txt", summaryFile = "summaryBlocked.csv"):
        '''Output
        We want a couple of things out of this output.  A summary file of P1 and P2 variables per question permutation.
        The texts for both P1 and P2 that will be copied in for each numbered question, and the appropriately-numbered block ID'''

        data=self.permuteBlockedNew()
        f = open(dataFile, 'w')
        s = open(summaryFile, 'w')

        canIDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # sloppy yar
        rurIDS = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
        aboIDS = [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 61, 62, 63]
        immIDS = [96, 97, 98, 99, 100, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
        
        writer = csv.writer(s, lineterminator='\n')
        writer.writerow(["qid", "P1id", "P2id", "P1region", "P1urban", "P1status", "P1income", "P1language", "P2region", "P2urban", "P2status", "P2income", "P2language"])

        questionCounter = 1


##        varList = ["region", "urban", "status", "income", "language"]
##        
##        iterHolder = []

        # csvHelper function

        def csvHelper(qnum, id1, id2, tempText1, tempText2):
            tempRow = []
            tempRow.append(str(qnum))
            tempRow.append(str(id1))
            tempRow.append(str(id2))

            # P1
            
            for r in self.regionList:
                if r in tempText1:
                    tempRow.append(self.regionNames[self.regionList.index(r)])
            for u in self.urbanList:
                if u in tempText1:
                    tempRow.append(self.urbanNames[self.urbanList.index(u)])

            if len(tempRow)==4:
                tempRow.append("NA")
                
            for t in self.statusList:
                if t in tempText1:
                    tempRow.append(self.statusNames[self.statusList.index(t)])
            if len(tempRow)==5:
                tempRow.append("NA")
                
            for n in self.incomeList:
                if n in tempText1:
                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
            for l in self.languageList:
                if l in tempText1:
                    tempRow.append(self.languageNames[self.languageList.index(l)])

            # P2
            
            for r in self.regionList:
                if r in tempText2:
                    tempRow.append(self.regionNames[self.regionList.index(r)])
            for u in self.urbanList:
                if u in tempText2:
                    tempRow.append(self.urbanNames[self.urbanList.index(u)])
            if len(tempRow)==9:
                tempRow.append("NA")
                
            for t in self.statusList:
                if t in tempText2:
                    tempRow.append(self.statusNames[self.statusList.index(t)])
            if len(tempRow)==10:
                tempRow.append("NA")
                
            for n in self.incomeList:
                if n in tempText2:
                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
            for l in self.languageList:
                if l in tempText2:
                    tempRow.append(self.languageNames[self.languageList.index(l)])

            return tempRow
            

        # Canada block -- 400 permutations

        for P1 in canIDS:
            for P2 in canIDS:
                if P1 != P2:
                    tempText1 = data["can"][P1]
                    tempText2 = data["can"][P2]

                    # text file
                    f.write("C"+str(questionCounter)+'\n')
                    f.write('P1\n')
                    f.write(tempText1+'\n')
                    f.write('P2\n')
                    f.write(tempText2+'\n\n')

                    # csv file
                    tempRow = csvHelper(("C"+str(questionCounter)), P1, P2, tempText1, tempText2)
                    writer.writerow(tempRow)

                    questionCounter +=1

        # Urban/rural block -- 1600 permutations

        for P1 in rurIDS:
            for P2 in rurIDS:
                if P1 != P2:
                    tempText1 = data["rur"][P1]
                    tempText2 = data["rur"][P2]

                    # text file
                    f.write("R"+str(questionCounter)+'\n')
                    f.write('P1\n')
                    f.write(tempText1+'\n')
                    f.write('P2\n')
                    f.write(tempText2+'\n\n')

                    # csv file
                    tempRow = csvHelper(("R"+str(questionCounter)), P1, P2, tempText1, tempText2)
                    writer.writerow(tempRow)

                    questionCounter +=1

        # Aboriginal block -- 400 permutations (with halved alternation of sides)

        for P1 in aboIDS:
            for P2 in canIDS:
                if P1 != P2:
                    tempText1 = data["abo"][P1]
                    tempText2 = data["can"][P2]

                    # now we have to go half and half with the order

                    seed = random.choice([1, 2])

                    if seed==1:

                        # text file
                        f.write("A"+str(questionCounter)+'\n')
                        f.write('P1\n')
                        f.write(tempText2+'\n')
                        f.write('P2\n')
                        f.write(tempText1+'\n\n')

                        # csv file
                        tempRow = csvHelper(("A"+str(questionCounter)), P2, P1, tempText2, tempText1)
                        writer.writerow(tempRow)

                        questionCounter +=1


                    elif seed==2:

                        # text file
                        f.write("A"+str(questionCounter)+'\n')
                        f.write('P1\n')
                        f.write(tempText1+'\n')
                        f.write('P2\n')
                        f.write(tempText2+'\n\n')

                        # csv file
                        tempRow = csvHelper(("A"+str(questionCounter)), P1, P2, tempText1, tempText2)
                        writer.writerow(tempRow)

                        questionCounter +=1

        # immigrant block -- 400 permutations (with halved alternation of sides)

        for P1 in immIDS:
            for P2 in canIDS:
                if P1 != P2:
                    tempText1 = data["imm"][P1]
                    tempText2 = data["can"][P2]

                    # now we have to go half and half with the order

                    seed = random.choice([1, 2])

                    if seed==1:

                        # text file
                        f.write("I"+str(questionCounter)+'\n')
                        f.write('P1\n')
                        f.write(tempText2+'\n')
                        f.write('P2\n')
                        f.write(tempText1+'\n\n')

                        # csv file
                        tempRow = csvHelper(("I"+str(questionCounter)), P2, P1, tempText2, tempText1)
                        writer.writerow(tempRow)

                        questionCounter +=1


                    elif seed==2:

                        # text file
                        f.write("I"+str(questionCounter)+'\n')
                        f.write('P1\n')
                        f.write(tempText1+'\n')
                        f.write('P2\n')
                        f.write(tempText2+'\n\n')

                        # csv file
                        tempRow = csvHelper(("I"+str(questionCounter)), P1, P2, tempText1, tempText2)
                        writer.writerow(tempRow)

                        questionCounter +=1
                
                
        
##        for i in self.IDNum:
##            tempText = data[i]
##            # text file
##            f.write("G"+str(i)+'\n')
##            f.write(data[i]+'\n\n')
##
##            # csv file
##            tempRow = []
##            tempRow.append("G"+str(i))
##            iterHolder.append(("G"+str(i)))
##            
##
##            for r in self.regionList:
##                if r in tempText:
##                    tempRow.append(self.regionNames[self.regionList.index(r)])
##            for u in self.urbanList:
##                if u in tempText:
##                    tempRow.append(self.urbanNames[self.urbanList.index(u)])
##            for t in self.statusList:
##                if t in tempText:
##                    tempRow.append(self.statusNames[self.statusList.index(t)])
##            for n in self.incomeList:
##                if n in tempText:
##                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
##            for l in self.languageList:
##                if l in tempText:
##                    tempRow.append(self.languageNames[self.languageList.index(l)])
##            writer.writerow(tempRow)
##
##        x = list(itertools.islice(itertools.combinations(iterHolder, 2), 100000))

        # close properly
        f.close()
        s.close()


    def outputFinal(self, dataFile = "dataFinal.txt", summaryFile = "summaryFinal.csv"):
        '''Output:
        A summary file of P1 and P2 variables per question permutation.
        The texts for both P1 and P2 that will be copied in for each numbered question--with Player A and Player B substituted based upon order'''

        data=self.permute()
        f = open(dataFile, 'w')
        s = open(summaryFile, 'w')

        canIDS=list(range(1, 41))
        
        writer = csv.writer(s, lineterminator='\n')
        writer.writerow(["qid", "P1id", "P2id", "P1region", "P1urban", "P1income", "P1language", "P2region", "P2urban", "P2income", "P2language"])

        questionCounter = 1




##        varList = ["region", "urban", "status", "income", "language"]
##        
##        iterHolder = []

        # csvHelper function

        def csvHelper(qnum, id1, id2, tempText1, tempText2):
            tempRow = []
            tempRow.append(str(qnum))
            tempRow.append(str(id1))
            tempRow.append(str(id2))

            # P1
            
            for r in self.regionList:
                if r in tempText1:
                    tempRow.append(self.regionNames[self.regionList.index(r)])
            for u in self.urbanList:
                if u in tempText1:
                    tempRow.append(self.urbanNames[self.urbanList.index(u)])

            for n in self.incomeList:
                if n in tempText1:
                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
            for l in self.languageList:
                if l in tempText1:
                    tempRow.append(self.languageNames[self.languageList.index(l)])

            # P2
            
            for r in self.regionList:
                if r in tempText2:
                    tempRow.append(self.regionNames[self.regionList.index(r)])
            for u in self.urbanList:
                if u in tempText2:
                    tempRow.append(self.urbanNames[self.urbanList.index(u)])

            for n in self.incomeList:
                if n in tempText2:
                    tempRow.append(self.incomeNames[self.incomeList.index(n)])
            for l in self.languageList:
                if l in tempText2:
                    tempRow.append(self.languageNames[self.languageList.index(l)])

            return tempRow
            


        for P1 in canIDS:
            for P2 in canIDS:
                if P1 != P2:
                    tempText1 = data[P1]
                    tempText1=tempText1.replace("QQQ", "Player A")
                    tempText2 = data[P2]
                    tempText2=tempText2.replace("QQQ", "Player B")

                    tempMain = self.questionHTML
                    tempMain=tempMain.replace("PLACEHOLDERA", tempText1)
                    tempMain=tempMain.replace("PLACEHOLDERB", tempText2)
                    

                    # text file
                    f.write("C"+str(questionCounter)+'\n')
                    f.write(tempMain+'\n\n')

                    # csv file
                    tempRow = csvHelper(("C"+str(questionCounter)), P1, P2, tempText1, tempText2)
                    writer.writerow(tempRow)

                    questionCounter +=1

    

        # close properly
        f.close()
        s.close()





