import sys
from PyQt5 import QtCore, QtGui

def print_to_output(textBrowser, print_str):
    textBrowser.setText(textBrowser.toPlainText() + "\n" + print_str)

def start_csv_conversion(self, fname):
    print_to_output(self.textBrowser, "Detected CSV file, starting conversion process...")

    import xlrd
    import csv
    import pandas
    import sqlite3

    print_to_output(self.textBrowser, "Initializing '" + fname + "'...")
    wb = xlrd.open_workbook(fname)
    sheets = wb.sheet_names()
    sh = wb.sheet_by_name(str(sheets[0]))
    name = fname[:fname.find('.')]
    csvname = name + '.csv'

    your_csv_file = open(csvname, 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        try:
            wr.writerow(sh.row_values(rownum))
        except(UnicodeEncodeError):
            pass

    your_csv_file.close()

    print_to_output(self.textBrowser, "CSV file '" + csvname + "' created successfully.")

    dbfile = name + '.sqlite'
    cnx = sqlite3.connect(dbfile)
    print_to_output(self.textBrowser, "Initializing '" + csvname + "'...")
    df = pandas.read_csv(csvname)
    df.to_sql('gtd', cnx)

    print_to_output(self.textBrowser, "SQLite database '" + dbfile + "' created successfully.")

    return dbfile