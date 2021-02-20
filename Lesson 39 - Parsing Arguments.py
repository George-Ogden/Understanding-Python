from argparse import ArgumentParser

parser = ArgumentParser(description="Add or multiply numbers")
parser.add_argument("numbers",metavar="N",type=int,nargs="+",help="Integers to add or multiply")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--add","-a",action="store_true",help="Add the numbers")
group.add_argument("--multiply","-m",action="store_true",help="Multiply the numbers")
arguments = parser.parse_args()

if arguments.multiply:
    total = 1
    for number in arguments.numbers:
        total *= int(number)
else:
    total = 0
    for number in arguments.numbers:
        total += int(number)
print("Total =", total)
