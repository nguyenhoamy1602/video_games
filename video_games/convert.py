#changes the pandas CSV ver of pivot table into arrays that highcharts can read
def convertCSVFormat(file, cat1, cat2):
    lines = file.split('\n')
    aggr = True
    xLabels = []
    yLabels = []
    label = True
    data = []
    x = 0
    for line in lines:
        list = line.split(',')
        if aggr:
            aggr = False
        else:
            if label:
                label = False
                for item in list[1:]:
                    if str(cat2) == 'Year':
                        item = int(float(item))
                        yLabels.append(str(item))
                    else:
                        yLabels.append(item)
            else:
                if str(cat1) == 'Year' and cat1 != list[0]:
                    try:
                        item = int(float(list[0]))
                        xLabels.append(str(item))
                    except ValueError:
                        xLabels.append(list[0])
                elif cat1 != list[0]:
                    xLabels.append(list[0])
                y = 0
                if cat1 != list[0]:
                    for item in list[1:]:
                        try:
                            item = float(item)
                            data.append([x, y, round(item,2)])
                        except ValueError:
                            data.append([x, y, 0])
                        y += 1
                    x += 1


    return(xLabels, yLabels, data)