pasta = []
juice = []

for i in range(3):
    pasta.append(int(input()))

for i in range(2):
    juice.append(int(input()))

pasta.sort()
juice.sort()

print('{0:.1f}'.format((pasta[0] + juice[0]) * 1.1))
