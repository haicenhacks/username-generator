import argparse


def main(infile='names.txt', name=None, outfile='usernames.txt'):
    names = []
    if infile:
        try:
            with open(infile, 'r') as fio:
                lines = fio.readlines()
                starting_names = [l.rstrip() for l in lines]
        except FileNotFoundError:
            print(f"input file '{infile}' does not exist")
            return

    else:
        starting_names = [name]

    for l in starting_names:
        num_spaces = l.count(' ')
        l = l.split(' ')
        if len(l) > 3:
            print('mangling of more than first, middle, last name is unsupported at this time')
            continue
        l_first = l[0].lower()
        l_last = l[-1].lower()

        names.append(f"{l_first}.{l_last}")
        names.append(f"{l_first}{l_last}")
        names.append(f"{l_first[0]}.{l_last}")
        names.append(f"{l_first[0]}{l_last}")
        names.append(f"{l_first}.{l_last[0]}")
        names.append(f"{l_first}_{l_last}")
        names.append(f"{l_first}")
        names.append(f"{l_last}")
        if len(l) == 3:
            l_middle = l[1].lower()
            names.append(f"{l_first}{l_middle[0]}.{l_last}")
            names.append(f"{l_first}{l_middle[0]}{l_last}")
            names.append(f"{l_first[0]}{l_middle[0]}{l_last}")
            names.append(f"{l_first[0]}{l_middle[0]}.{l_last}")
            names.append(f"{l_first[0]}.{l_middle[0]}.{l_last}")

            names.append(f"{l_first[0]}{l_middle[0]}{l_last}")
            names.append(f"{l_first}.{l_middle[0]}.{l_last[0]}")
            names.append(f"{l_first}_{l_middle[0]}_{l_last}")

        if outfile:
            with open(outfile, 'w') as fio:
                for n in names:
                    fio.write(f"{n}\n")
        else:
            for n in names:
                print(f"{n}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate usernames from first and last names")
    parser.add_argument('-i', help="input file containing a list of names")
    parser.add_argument('-N', help="a single name (enclosed in quotes)")
    parser.add_argument('-o', help="where to output results")

    args = parser.parse_args()
    main(infile=args.i, outfile=args.o, name=args.N)
