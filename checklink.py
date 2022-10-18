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
    for index, row in df.iterrows():
        rn = row["RecordNumber"]
        tag = row["Tag"]
        c = row["content"]
        if tag == 20:
            print("original",c)
            if "a" in c:
                isbn = c.split("a")[1].replace("$q(electronic book)", "")
                if "(" in isbn:
                    isbn = isbn.split("(")[0].strip()
                print("a")
            if "z" in c:
                isbn = c.split("z")[1]
                if "(" in isbn:
                    isbn = isbn.split("(")[0].strip()
                if "$" in isbn:
                    isbn = isbn.split("$")[0].strip()
                print("z")
            print(isbn)
            print()
            raw_url = df[(df['Tag'] == 856) & (df['RecordNumber'] == rn)].content.values[0]
            url = raw_url.split("$z")[0].replace("$u", "")
            d[isbn] = url
    return d, isbnl

def go(txtisbn, dffn, finalfn):
    d, isbnl = check(txtisbn, dffn)
    urll = []
    for i in isbnl:
        i = i.replace(".", "")
        if i != "":
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
