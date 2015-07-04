#!/usr/local/bin/python
# HUFFMAN DATA COMPRESSION

codes = {}

def frequency (string) :                        # get frequency dict of alphabets
    freq = {}
    for chars in string :
        freq[chars] = freq.get(chars, 0) + 1
    return freq

def sortFreq (freq) :           # get list of tuples of frequency and alphabet
    tuples = []
    for k, v in freq.items() :
        tuples.append((v, k))
    tuples.sort()
    return tuples

def buildTree (tuples) :        # building top to bottom tree of alphabets..refer notes
    while len(tuples) > 1 :
        leastTwo = tuple(tuples[0:2])
        theRest = tuples[2:]
        combinedFreq = leastTwo[0][0] + leastTwo[1][0]
        tuples = theRest + [(combinedFreq, leastTwo)]
        tuples.sort()
    return tuples[0]            # returns single element tree inside the list

def trimTree (tree) :           # trimming off the combined freq in the tree
    p = tree[1]
    if type(p) == str :
        return p
    else :
        return (trimTree(p[0]), trimTree(p[1]))

def assignCodes (node, pat = '') :  # assign codes to alphabets
    global codes
    if type(node) == str :
        codes[node] = pat
    else :
        assignCodes(node[0], pat + '0')
        assignCodes(node[1], pat + '1')

def encode (string) :           # encoding string using codes dict
    global codes
    output = ""
    for char in string :
        output += codes[char]
    return output

def decode (tree, encoded_str) :    # decoding encoded string using tree
    p = tree
    output = ''
    for bit in encoded_str :
        if bit == '0' :
            p = p[0]
        else :
            p = p[1]
        if type(p) == str :
            output += p
            p = tree            # if string found...return to root of tree
    return output

def main () :
    string = raw_input("Enter a string :- ")

    freqs = frequency(string)
    tuples = sortFreq(freqs)
    tree = buildTree(tuples)
    tree = trimTree(tree)
    print tree
    assignCodes(tree)
    encoded_str = encode(string)
    original = decode (tree, encoded_str)
    print '\n'
    print "original string :- %s" %(original)
    print '\n'
    print "encoded string :- %s" %(encoded_str)
    print '\n'
    print 'CODES:\n'
    print codes
    print '\n'

if __name__ == "__main__" :
    main()
