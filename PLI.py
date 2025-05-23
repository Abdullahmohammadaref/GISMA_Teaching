def main():
    user_input = str(input("Type some letters:"))
    output = list(''.join(user_input))
    print(output)

    letters = {}

    j = 0
    for i in output:
        letters.update({i: [].append(j)})
        j = j + 1

    print(letters)


if __name__=='__main__':
    main()

    ###  cross columnt combination     , parraler processing, mutlithreadding    PLI   A*

    ## reduce number of modules to train modules

    ### create pli s and see if you can run in threadding styel