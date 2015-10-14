from __future__ import print_function
import __builtin__


class Matrix:
    def __init__(self, rows = 0, columns = 0):
        if not rows or not columns:
            self.matrix = []
            self.columns = 0
            self.rows = 0
        else:
            self.matrix = [[0 for i in range(columns)] for i in range(rows)];
            self.rows = len(self.matrix)
            self.columns = len(self.matrix[0])

    def modifyElement(self, row, column, element):
        row -= 1
        column -= 1
        try: self.matrix[row][column] = element; return True;
        except:return False;

    def modifyRow(self, row = False, elements = False):
        if not elements or not row: return False;
        else:
            try: self.matrix[row - 1] = [elements for i in range(self.columns)]; return True;
            except IndexError: return (False, "Index Error");
        return False;

    def modifyColumn(self, column = False, elements = False):
        column -= 1
        if not elements or not column and not column == 0 :return False;
        else:
            try:
                for row in range(len(self.matrix)):
                     self.matrix[row][column] = elements;
                     return True;
            except IndexError: return (False, "Index Error")
        return False;

    def getRow(self, rowNumber):
        rowNumber -= 1;
        try:
            return self.matrix[rowNumber];
        except IndexError: return (False, "Index Error");
        return False;

    def getColumn(self, columnNumber):
        columnNumber -= 1;
        try:
            return list(self.matrix[row][columnNumber] for row in range(len(self.matrix)));
        except IndexError: return (False, "Index Error");
        return False;

    def getSuperiorTriangle(self):
        return list((coordenate[0], index) for coordenate in self.getDiagonal() for index in range(coordenate[1] + 1, len(self.matrix)))

    def getInferiorTriangle(self):
        return list((index, coordenate[1]) for coordenate in self.getDiagonal() for index in range(coordenate[0] + 1, len(self.matrix)))

    def addRow(self, afterRow = False, element = 0):
        """This method add a row after the row parameter, with the elements parameter"""
        if afterRow:
            try:
                self.matrix.insert(afterRow, [element for i in range(self.columns)]);self.rows = len(self.matrix);return True;
            except IndexError: return (False, "Index Error")
        if not afterRow:
            try:
                self.matrix.append([element for i in range(self.columns)]);self.rows = len(self.matrix);return True;
            except: return (False, "Index Error");
        return False;

    def addColumn(self, afterColumn = False, element = 0):
        """This method add a column after the column parameter, with the elements parameter"""
        if afterColumn :
            try:
                for row in range(len(self.matrix)): self.matrix[row].insert(afterColumn, element);self.columns = len(self.matrix[0]);
            except IndexError: return (False, "Index Error")
        elif not afterColumn:
            try:
                for row in range(len(self.matrix)): self.matrix[row].append(element);self.columns = len(self.matrix[0]);
            except IndexError: return (False, "Index Error")
        return False;

    def getDiagonal(self):
        diagonal = list(zip(range(0, len(self.matrix)), range(0, len(self.matrix[0]))))
        return diagonal

    def __repr__(self):
        string = ""
        for row in self.matrix:
            for element in row:
                string += "{:^5d}" .format  (element)
            string += "\n"
        return string;
