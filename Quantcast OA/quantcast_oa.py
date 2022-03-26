import sys

#main function to scan in arguments
def main():
    input = sys.argv
    csvFile = input[1]
    date = input[3]
    mostActiveCookie(csvFile, date)


#scan in the csv data into dict
def scan(fn):
    with open(fn, 'r') as f:
        d = {}
        for line in f:
            if 'cookie' not in line:
                words = line.split(',')
                cookie = words[0]
                date = words[1][:words[1].index('T')]
                if date not in d:
                    d[date] = [cookie]
                else:
                    d[date].append(cookie)
    return d

#given an array, finds the most frequent elements
def mostFrequent(arr):
    d = {}
    m = 0
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        m = max(m, d[i])
    ans = []
    for k, v in d.items():
        if(v == m):
            print(k)
    

#runs the helper methods
def mostActiveCookie(fn, date):
    cookies = sorted(scan(fn)[date])
    return mostFrequent(cookies)


if __name__ == "__main__":
    main()