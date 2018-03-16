import sys
from PyQt5 import QtCore, QtGui

def print_to_output(textBrowser, print_str):
    textBrowser.setText(textBrowser.toPlainText() + "\n" + print_str)

def attacks_by_count(self, con, n, visualize=False):
    print_to_output(self.textBrowser, "Retrieving data...")
    query = "SELECT COUNT(te.eventid),loc.country FROM Location loc, TerrorEvent te, Country c WHERE loc.id = te.eventid GROUP BY loc.country ORDER BY COUNT(te.eventid) DESC LIMIT " + n
    curr = con.execute(query)
    print_to_output(self.textBrowser, "Data retrieved.\n")

    if(visualize):
        words = list()
        counts = dict()

        for row in curr:
            cid = row[1]
            country = con.execute("SELECT cname FROM Country WHERE cid=" + cid)
            word = country.fetchone()[0]
            words.append(word)
            counts[word] = long(row[0])

        bigsize = 80
        smallsize = 20

        highest = None
        lowest = None
        for w in words:
            if highest is None or highest < counts[w] :
                highest = counts[w]
            if lowest is None or lowest > counts[w] :
                lowest = counts[w]

        fhand = open('gtdcountries.js','w')
        fhand.write("gword = [")
        first = True
        for k in words:
            if not first : fhand.write( ",\n")
            first = False
            size = counts[k]
            size = (size - lowest) / float(highest - lowest)
            size = int((size * bigsize) + smallsize)
            fhand.write("{text: '"+k+"', size: "+str(size)+"}")
        fhand.write( "\n];\n")
        return

    print_to_output(self.textBrowser, "ATTACKS\t\tCOUNTRY")
    print_output = ''
    for row in curr:
        cid = row[1]
        country = con.execute("SELECT cname FROM Country WHERE cid=" + cid)
        print_output += str(row[0]) + "\t\t" + country.fetchone()[0] + "\n"
    print_to_output(self.textBrowser, print_output)

def attacks_by_casualties(self, con, n):
    print_to_output(self.textBrowser, "Retrieving data...")
    query = "SELECT SUM(te.nkill),loc.country FROM Location loc, TerrorEvent te, Country c WHERE loc.id = te.eventid GROUP BY loc.country ORDER BY SUM(te.nkill) DESC LIMIT " + n
    curr = con.execute(query)
    print_to_output(self.textBrowser, "Data retrieved.\n")

    print_to_output(self.textBrowser, "CASUALTIES\t\tCOUNTRY")
    print_output = ''
    for row in curr:
        cid = row[1]
        country = con.execute("SELECT cname FROM Country WHERE cid=" + cid)
        print_output += str(row[0]) + "\t\t" + country.fetchone()[0] + "\n"
    print_to_output(self.textBrowser, print_output)

def attacks_by_dates(self, con, start, end, map=False):
    print_to_output(self.textBrowser, "\nDate format is YYYY-MM-DD.")
    print_to_output(self.textBrowser, "Retrieving data...")
    query = "SELECT te.eventid, te.summary, t.day, te.nkill FROM TerrorEvent te, Time t WHERE te.eventid = t.id AND t.day >= '" + start + "' AND t.day <= '" + end + "'"
    curr = con.execute(query)
    print_to_output(self.textBrowser, "Data retrieved.\n")

    strarr = ''
    if(map):
        print_to_output(self.textBrowser, "Generating map...")
        strarr += "       ['Latitude', 'Longitude', 'Casualties'],\n"
        lastrow = None
        for row in curr:
            id = str(long(row[0]))
            query = "SELECT loc.lat,loc.long FROM Location loc, TerrorEvent te WHERE loc.id = " + id
            geo = con.execute(query)
            for r in geo:
                if(r[0] is None or r[1] is None): continue
                casualties = row[3]
                if(casualties is None): casualties = 0
                strarr += '       [' + str(r[0]) + ', ' + str(r[1]) + ', ' + str(int(casualties)) + '],\n'
                break
        strarr = strarr[:len(strarr)-2]

        with open('mapframe.html', 'r') as f_in:
            with open('map.html','w') as f_out:
                for line_no, line in enumerate(f_in, 1):
                    if line_no == 10:
                        f_out.write(strarr)
                    f_out.write(line)
        
        print_to_output(self.textBrowser, "Map generated.'.")
        return

    print_output = ''
    for row in curr:
        print_output += "ID: " + str(long(row[0])) + "\nDetails: " + str(row[1]) + "\n"
    print_to_output(self.textBrowser, print_output)