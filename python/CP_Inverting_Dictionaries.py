#!/usr/bin/python2.7
'''
Created on Jul 20, 2012
Take a dictionary as input and return one as output, but the values are now the keys and vice versa.
@author: MNickey
'''

mydict = {'Alpha': 1, 'Beta': 2, 'Gamma': 3, 'Delta':4, 'E-psilon': 5, 'Zeta' : 6, 'Eta': 7, 'Theta':8, 'Lola':9, 
          'Kappa':10, 'Lambda':11, 'Mu':12, 'Nu':13, 'Xi':14, 'O-micron':15, 'Pi':16, 'Rho':17, 'Sigma':18, 'Tau':19,
          'U-psilon':20, 'Phi':21, 'Chi':22, 'Psi':23, 'O-mega':24 }
new_dict = {}

# Get the dictionary for input
def getDict():
    new_dict = dict((value, key) for key, value in mydict.iteritems())
    print new_dict
    return

if __name__ == '__main__':
    getDict()
    