import pandas as pd
import requests, sys, validators

# Preparing dummy data
def check(txtisbn, dffn):
    isbnf = open(txtisbn, "r")
    data = isbnf.read()
    isbnl = data.split("\n")
    isbnl = isbnl[1:]
    df = pd.read_csv(dffn)
    df.columns = ['Tag', 'content', 'Indicators', 'RecordNumber']
    d = {}
    # d['9781414464411'] = "https://link.gale.com/apps/pub/2QZS/SATA?sid=gale_marc&u=san96005"
    # d["9781414482378"] = "https://link.gale.com/apps/pub/3LHC/SATA?sid=gale_marc&u=san96005"
    for index, row in df.iterrows():
        rn = row["RecordNumber"]
        tag = row["Tag"]
        c = row["content"]
        if tag == 20:
            if "a" in c:
                isbn = c.split("a")[1].replace("$q(electronic book)", "")
            if "z" in c:
                isbn = c.split("z")[1]
            raw_url = df[(df['Tag'] == 856) & (df['RecordNumber'] == rn)].content.values[0]
            url = raw_url.split("$z")[0].replace("$u", "")
            d[isbn] = url
    return d, isbnl

def go(txtisbn, dffn, finalfn):
    d, isbnl = check(txtisbn, dffn)
    urll = []
    for i in isbnl:
        i = i.replace(".", "")
        urll.append(d[i])
    with open(finalfn, 'w') as fp:
        for item in urll:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')

if __name__ == "__main__":
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    go(sys.argv[1],sys.argv[2],sys.argv[3])
