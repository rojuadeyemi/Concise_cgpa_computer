def cgpa():
    try:
        p = int(input("\nEnter the number of courses you wish to compute cgpa for --> ").strip())
    except:
        while True:
            try:
                p = int(input("\nRe-enter the number of courses you wish to compute cgpa for --> ").strip())
            except:
                pass
            else:
                break

    r = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    x = []
    u = []
    t = []
    m = p
    while 0 < p:
        if p == m:
            a = input("\nEnter the first course code --> ").upper()
            while not (''.join(a.split()).isalnum()):
                a = input("\nRe-enter the course code --> ").upper()
                print(''.rjust(33, '*'))
        else:
            a = input("\nEnter the next course code --> ").upper()
            while not (''.join(a.split()).isalnum()):
                a = input("\nRe-enter the course code --> ").upper()
                print(''.rjust(33, '*'))
        try:
            b = int(input("Enter the unit of the course entered above --> "))
        except:
            while True:
                try:
                    b = int(input("Re-enter the unit of the course entered above --> "))
                except:
                    pass
                else:
                    break

            print(''.rjust(50, '~'))

        e = input("Enter the grade of the course entered --> ").upper()
        while e not in 'ABCDEF':
            e = input("Re-enter the grade of the course entered --> ").upper()
        print(''.rjust(44, '#'), '\n')
        print(('Course \"%s\" saved!' % a).center(44))

        t.append(e)  # for grades
        x.append(a)  # for course codes
        u.append(b)  # for units
        p -= 1

    result = 0
    for num in range(m):
        result += r[t[num]] * u[num]

    print('\n\n')
    print("Summary Table")
    print("".rjust(38, '='))
    print("S/N", "Course-code".rjust(10), "Unit".rjust(8), "Grade".rjust(13))
    print(''.rjust(38, '-'))
    for y in range(len(t)):
        print(y + 1, x[y].rjust(10), str(u[y]).rjust(10), t[y].rjust(12))
        print(''.rjust(38, '-'))
    print(''.rjust(61, '='))
    print("Number of courses\t", "Cumulative-Total\t", "Total Units\t", "CGPA", '\n')
    print(str(m).rjust(9), str(result).rjust(20), str(sum(u)).rjust(16), str("%.2f" % (result / sum(u))).rjust(13))
    print(''.rjust(61, '='))


cgpa()
