def read_file(filename):
    file = open(filename)
    filee = file.read()
    print(filee)
read_file("timestamp.txt")