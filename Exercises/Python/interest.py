sps = []
ir = []

with open('SP500.txt') as sp:
        idx = 6
        idy = 2016
        for i in sp.readlines():
            while idx is not 5:
                if i.startswith(str(idx)) and str(idy) in i:
                    temp = i.split(',')
                    sp1 = float(temp[1])
                    ir1 = float(temp[5])
                    sps.append(sp1)
                    ir.append(ir1)
                    idx += 1
                elif idx == 13:
                    idx = 1
                    idy = 2017
                    continue
                else:
                    break

for i in sp.readlines():
    if i.startswith('5') and '2017' in i:
        temp = i.split(',')
        sp1 = float(temp[1])
        ir1 = float(temp[5])
        sps.append(sp1)
        ir.append(ir1)

mean = 0
for i in sps:
    mean += i

mean_SP = mean / float(len(sps))
max_interest = max(ir)
