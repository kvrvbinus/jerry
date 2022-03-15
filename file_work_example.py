
FILE_PATH="/home/roman/fite.txt"


def main():
    print("HELLO WORLD")
    print(FILE_PATH)
    tmp_file=open(FILE_PATH,'r')
    data=tmp_file.read()

    print(data)
    print ("-------")

    for line in data.split("\n"):
        out_str="LINE:\""+line+"\""
        print(out_str)








if __name__ == '__main__':
    main()