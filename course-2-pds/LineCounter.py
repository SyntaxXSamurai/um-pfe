try:
    fName = input('Enter the file name: ')
    file = open(fName)
    count = 0

    for line in file:
        # Change in relation to the .txt file
        if line.startswith('Subect:'):
            count += 1

    print('Number of Lines in ' + fName + ': ' + count)
except:
    print('File name invalid')