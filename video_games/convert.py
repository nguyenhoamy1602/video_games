def convertCSVFormat(file, cat1, cat2):
    lines = file.split('\n')
    aggr = True
    value = True
    yLabels = []
    xLabels = []
    values = []
    x = 0
    for line in lines:
        items = line.split(',')
        if aggr:
            aggr = False
        else:
            if value:
                value = False
                for item in items[1:]:
                    if str(cat2) == 'Year':
                        item = int(float(item))
                        yLabels.append(str(item))
                    else:
                        yLabels.append(item)
            else:
                if str(cat1) == 'Year' and cat1 != items[0]:
                    try:
                        item = int(float(items[0]))
                        xLabels.append(str(item))
                    except ValueError:
                        xLabels.append(items[0])
                elif cat1 != items[0]:
                    xLabels.append(items[0])
                y = 0
                if cat1 != items[0]:
                    for item in items[1:]:
                        try:
                            item = float(item)
                            values.append([x, y, round(item,2)])
                        except ValueError:
                            values.append([x, y, 0])
                        y += 1
                    x += 1


    return(xLabels, yLabels, values)