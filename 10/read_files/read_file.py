filename = 'learning_python.txt'

with open(filename) as file_object:
    file = file_object.read()
    file_object.seek(0,0)
    lines = file_object.readlines()
    file_object.seek(0,0)
    print('----- read ------')
    print(file.replace('Python','C'))
    print('----- lines ------')
    for line in file_object:
        print(line.rstrip())
print('----- out of wirth ------')
for line in lines:
    print(line.replace('Python','C').rstrip())
