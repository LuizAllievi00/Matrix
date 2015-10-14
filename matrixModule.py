# -*- coding: utf-8 -*-
from matrix import *

def isMatrix(matrix):
    """This function verifies if the given argument is a matrix"""
    if isinstance(matrix, Matrix):return True;
    return False;

def squareMatrix(matrix):
    """A square matrix is a matrix that the number of rows is the same that the number of the columns"""
    if isMatrix(matrix):
        if matrix.rows == matrix.columns: return True;
    return False;

def triangleMatrix(matrix):
    """A triangle matrix is a matrix that have all superior or inferior null elements by the diagonal"""
    if isMatrix(matrix) and squareMatrix(matrix):
                topDiagonal = matrix.getSuperiorTriangle()
                botDiagonal =  matrix.getInferiorTriangle()
    if len(list(matrix.matrix[element[0]][element[1]] for element in topDiagonal if matrix.matrix[element[0]][element[1]] == 0)) == len(topDiagonal): return True
    if len(list(matrix.matrix[element[0]][element[1]] for element in botDiagonal if matrix.matrix[element[0]][element[1]] == 0)) == len(botDiagonal): return True
    return False;

def diagonalMatrix(matrix):
    """A diagonal matrix is a matrix that have the same all diagonal elements"""
    control, control2 = False, False
    if isMatrix(matrix) and squareMatrix(matrix):
        topDiagonal = matrix.getSuperiorTriangle()
        botDiagonal =  matrix.getInferiorTriangle()
        if len(list(matrix.matrix[element[0]][element[1]] for element in topDiagonal if matrix.matrix[element[0]][element[1]] == 0)) == len(topDiagonal): control = True
        if len(list(matrix.matrix[element[0]][element[1]] for element in botDiagonal if matrix.matrix[element[0]][element[1]] == 0)) == len(botDiagonal): control2 = True
        if control and control2: return True
    return False;

def indentityMatrix(matrix):
    """A identity matrix is a matrix that have all diagonal elements equals to 1 and all other elementes equals to 0"""
    if squareMatrix(matrix) and triangleMatrix(matrix):
        if all(list(True if matrix.matrix[element[0]][element[1]] == 1 else False for element in matrix.getDiagonal())): return True;
        return False;


def nullMatrix(matrix):
    """A null matrix is a matrix that have all null elements"""
    if isMatrix(matrix):
        if all(list(True if matrix.matrix[row][column] == 0 else False for row in range(len(matrix.matrix)) for column in range(len(matrix.matrix[0])))): return True;
    return False;

def rowMatrix(matrix):
    """A row matrix is a matrix that have only one column"""
    if matrix.rows == 1: return True;
    return False;

def columnMatrix(matrix):
    """A column matrix is a matrix that have only one row"""
    if isMatrix(matrix):
        if matrix.columns == 1: return True;
    return False;

def transposedMatrix(matrix):
    newMatrix = Matrix(matrix.columns, matrix.rows);
    for line in range(1, matrix.rows + 1):
        for (element, column) in (zip(matrix.getRow(line), range(1, matrix.columns + 1))):
            newMatrix.modifyElement(column, line, element)
    return newMatrix

def symmetricMatrix(matrix):
    """Is very complex
    """
    if isMatrix(matrix):
        if squareMatrix(matrix) and all(list(True if matrix.matrix[coordenate[0]][coordenate[1]] == matrix.matrix[coordenate[1]][coordenate[0]] else False for coordenate in matrix.getSuperiorTriangle())): return True;
    return False;


m = Matrix(4,4);
m.modifyElement(3,2,34)
m.modifyElement(4,3,7)
m.modifyElement(4,2,8)
m.modifyRow(1,2)
print m
print 1
print transposedMatrix(m)
