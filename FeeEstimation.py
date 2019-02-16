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
#   ----> 1) Naive Solution : Search to calculate all combinaisons while taking into account the parents 
#   ----> 1) insertion
#   --------> Too many Case to make even without the parents Insertions (5214*5214) and before each intertion test if the weight is above 4.000.000 and insert parents transactions
#   --------> The complexity we have is like k*p + 2^n with n number of items and k*p some particular values concerning the parents search insertion so z * 2^n as a complexity
# Conclusion
# ------> problem similar to Knapsack Problem with two conditions and one constraint: 



if __name__ ==  "__main__": 

    a = parse_mempool_csv()
    Fees = [i.fee for i in a]
    Weight = [i.weight for i in a]
    print(len(Fees))
