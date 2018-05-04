def main():
    the_string = 'hello'
    the_string = 'goodbye'



    print('the length of the string is', len(the_string))

    for ch in the_string:
        if ch != ' ':
            print(ch, end='')

    index_num = 10

    if index_num < len(the_string) and index_num >= 0:
        print('the second character is', the_string[index_num])
    else:
        print('index out of range')

main()