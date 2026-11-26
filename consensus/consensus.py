from Bio import SeqIO
import numpy as np

def consensus(fastaFile):
    for dnaString in SeqIO.parse(fastaFile, "fasta"):
        dnaStringList = list(dnaString)

    A_prof = [0] * len(dnaStringList)
    T_prof = [0] * len(dnaStringList)
    G_prof = [0] * len(dnaStringList)
    C_prof = [0] * len(dnaStringList)

    for dnaString in SeqIO.parse(fastaFile, "fasta"):

        A_array = []
        T_array = []
        G_array = []
        C_array = []

        dnaStringList = list(dnaString)
    
        for nucleotide in dnaStringList:

            if nucleotide == "A":
                A_array.append(1)
            else: 
                A_array.append(0)

            if nucleotide == "T":
                T_array.append(1)
            else: 
                T_array.append(0)

            if nucleotide == "G":
                G_array.append(1)
            else: 
                G_array.append(0)

            if nucleotide == "C":
                C_array.append(1)
            else: 
                C_array.append(0)  

        A_prof = (np.array(A_array) + np.array(A_prof)).tolist()
        T_prof = (np.array(T_array) + np.array(T_prof)).tolist()
        G_prof = (np.array(G_array) + np.array(G_prof)).tolist()
        C_prof = (np.array(C_array) + np.array(C_prof)).tolist()

    profileMatrix = np.array([A_prof, T_prof, G_prof, C_prof])

    chars = ["A", "T", "G", "C"]
    consensusString = ""


    rows = len(profileMatrix)
    columns = len(profileMatrix[0])

    for column in range(columns):
        max_val = profileMatrix[0][column]
        max_row = 0 

        for row in range(1, rows):
            if profileMatrix[row][column] > max_val:
                max_val = profileMatrix[row][column]
                max_row = row

        consensusString += chars[max_row]

    print(consensusString)
    print("A: ", *A_prof)
    print("T: ", *T_prof)
    print("G: ", *G_prof)
    print("C: ", *C_prof)



consensus("consensus/DNA.fasta")