import os
directory = input('Enter the path to the directory: \n')
os.chdir(directory)
# print(os.getcwd())
count = int(input('Enter the initial file number: '))
#print(count)


def main():
    global count
    for file in os.listdir():
        fileName, fileExtension = os.path.splitext(file)
        fileName = "Page -" + str(count)
        count += 1

        nameUpdate = '{} {}'.format(fileName, fileExtension)
        os.rename(file, nameUpdate)

if __name__ == '__main__':
    main()