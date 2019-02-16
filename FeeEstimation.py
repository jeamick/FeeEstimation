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

if __name__ ==  "__main__": 
    a = parse_mempool_csv()
    for i in a:
        print (i.txid, i.fee, i.weight, i.parents)