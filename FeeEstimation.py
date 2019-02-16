# I. Understand the Question:
# --> We have an optimization problem where we need to maximum total fee for a miner by taking
#      into account two constraints:

# ----------> 1) Size of Block <= 4.000.000
# ----------> 2) A transaction which possessess parents may appear in a Block on if 
# ----------> 2) if all of its parents appear earlier in the block.

# II. Craft a Solution:
# II.1 Craft a  naive solution(brute-force):
#   ----> 1) Naive Solution : Search to calculate all combinaisons while taking into account the parents 
#   ----> 1) insertion
#   --------> Too many Case to make even without the parents Insertions (5214*5214) and before each intertion test if the weight is above 4.000.000 and insert parents transactions
#   --------> The complexity we have is like k*p + 2^n with n number of items and k*p some particular values concerning the parents search insertion so like 2^n as a complexity
# Conclusion
# ------> problem similar to Knapsack Problem with two conditions and one constraint.

# II.2 Craft a more elegant Solution:
#   ----> 1) Elegant Solution : let's use a dynamic programming solution
#   ----> 1) insertion
#   --------> Too many Case to make even without the parents Insertions (5214*5214) and before each intertion test if the weight is above 4.000.000 and insert parents transactions
#   --------> The complexity we have is like k*p + 2^n with n number of items and k*p some particular values concerning the parents search insertion so z * 2^n as a complexity
# Conclusion
# ------> problem similar to Knapsack Problem with two conditions and one constraint: 

class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        # TODO: add code to parse weight and parents fields
        self.weight = int(weight)
        self.parents = parents.strip().split(';')
        

def parse_mempool_csv():
    """Parse the CSV file and return a list of MempoolTransactions."""
    with open('mempool.csv') as f:
        return([MempoolTransaction(*line.strip().split(',')) for line in f.readlines()])


def max_total_fees_tab(S, W):
    """ Parse the CSV file and return a list of MempoolTransactions."""
    """ Need to modify this algotithm in order to have the parent transactions."""
    """ Ihope I will have time for that..."""
    mat = [[0] * (W + 1) for i in range(len(S))]
    for i in range(0, len(S)):
        for j in range(0, len(mat[0])):
            if S[i][1] > j:
                mat[i][j] = mat[i - 1][j]
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i - 1][int(j - S[i][1])] + S[i][2])
    return mat

def list_transactions(M, S, W):
    """Get List of transactions from the Maximum reward """

    transactions = []
    j = W
    i = len(S) - 1
    while M[len(S)-1][j] == M[len(S)-1][j-1]:
        j -= 1

    while j > 0:
        while i > 0 and M[i][int(j)] == M[i-1][int(j)]:
            i -= 1
        j = j-S[i][1]
        if j > -1:
            transactions.append(S[i])
        i -= 1
    return transactions


if __name__ ==  "__main__": 
    import pandas as pd
    import numpy as np


    a = parse_mempool_csv()
    Tx_Id = [i.txid  for i in a]
    Fees = [i.fee for i in a]
    Weight = [i.weight for i in a]
    Parents = [i.parents for i in a]
    Limit = 4000000 ## Weight Limit
    t = () 
    p = []
    for i in range(len(a)):
        l = np.asarray([str(Tx_Id[i]), int(Weight[i]), int(Fees[i])])
        # print(l)
        t = t + tuple(l)
        p.append(t)

    M = max_total_fees_tab(p, Limit)
    print("Max reward : ", M[len(p)-1][Limit]," BTC")

    list_tx = list_transactions(M ,p, Limit)
    block = pd.DataFrame(list(list_tx), columns=["TransactionID" ,"Size","Fee"])
    block['Size'] = block.Size.astype(int)
    block['TransactionID'] = block.TransactionID.astype(int)
    print(block)
    print("\nTotal block size: ",block['Size'].sum()," bytes")
    print("Total fees: ",block['Fee'].sum()," BTC")
    print("Reward for this block: ",block['Fee'].sum()," BTC")
