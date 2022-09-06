def main():
    infile=open('clients.txt','r')
    count = 0

    for line in infile:
        count+=1
        line=line.rstrip('\n')
        print(f"{count}. {line}")

main()