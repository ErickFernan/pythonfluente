colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ((c, s) for c in colors for s in sizes):
    print(tshirt)
