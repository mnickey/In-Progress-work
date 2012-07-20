#!/usr/bin/python2.7
'''
Created on Jul 16, 2012
Process the addition and multiplication of a pair of M by N matrices.
M and N must be of INT type.
@author: MNickey
'''

def getMSize():
    m_size = input("Enter the M size of the matrix: ")
    return m_size

def getNSize():
    n_size = input("Enter the N size of the matrix: ")
    return n_size

def doAddition(m_size, n_size):
    print "\nShowing the addition matrix"
    for x in xrange(m_size):
        for y in xrange(n_size):
            print "X is", x, "\tY is", y, "\tThe sum is:", (x + y) 
    return

def doMultiply(m_size, n_size):
    print "Showing the multiplication matrix"
    for x in xrange(m_size):
        for y in xrange(n_size):
            print "X is", x, "\tY is", y, "\tThe product is:", (x * y)

def begin():
    m_size = getMSize() + 1
    n_size = getNSize() + 1
    doAddition(m_size, n_size)
    print '=' * 30
    doMultiply(m_size, n_size)

if __name__ == '__main__':
    begin()
    