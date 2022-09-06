def main():
    import csv
    infile = open('steps.csv','r')
    csvfile=csv.reader(infile,delimiter=',')
    outfile=open('avg_steps.csv','w')

    next(csvfile)
    outfile.write('Month, Average Steps\n')

    months=['January','February','March','April','May','June','July','August','September','October','Novemeber','December']

    JanDays=0
    JanTotal=0
    FebDays=0
    FebTotal=0
    MarDays=0
    MarTotal=0
    AprDays=0
    AprTotal=0
    MayDays=0
    MayTotal=0
    JuneDays=0
    JuneTotal=0
    JulyDays=0
    JulyTotal=0
    AugDays=0
    AugTotal=0
    SepDays=0
    SepTotal=0
    OctDays=0
    OctTotal=0
    NovDays=0
    NovTotal=0
    DecDays=0
    DecTotal=0

    for line in csvfile:
        if int(line[0]) == 1:
            JanTotal+=int(line[1])
            JanDays+=1
        elif int(line[0]) == 2:
            FebTotal+=int(line[1])
            FebDays+=1
        elif int(line[0]) == 3:
            MarTotal+=int(line[1])
            MarDays+=1
        elif int(line[0]) == 4:
            AprTotal+=int(line[1])
            AprDays+=1
        elif int(line[0]) == 5:
            MayTotal+=int(line[1])
            MayDays+=1
        elif int(line[0]) == 6:
            JuneTotal+=int(line[1])
            JuneDays+=1
        elif int(line[0]) == 7:
            JulyTotal+=int(line[1])
            JulyDays+=1
        elif int(line[0]) == 8:
            AugTotal+=int(line[1])
            AugDays+=1
        elif int(line[0]) == 9:
            SepTotal+=int(line[1])
            SepDays+=1
        elif int(line[0]) == 10:
            OctTotal+=int(line[1])
            OctDays+=1
        elif int(line[0]) == 11:
            NovTotal+=int(line[1])
            NovDays+=1
        elif int(line[0]) == 12:
            DecTotal+=int(line[1])
            DecDays+=1

    JanAvg = JanTotal/JanDays
    FebAvg = FebTotal/FebDays
    MarAvg = MarTotal/MarDays
    AprAvg = AprTotal/AprDays
    MayAvg = MayTotal/MayDays
    JuneAvg = JuneTotal/JuneDays
    JulyAvg = JulyTotal/JulyDays
    AugAvg = AugTotal/AugDays
    SepAvg = SepTotal/SepDays
    OctAvg = OctTotal/OctDays
    NovAvg = NovTotal/NovDays
    DecAvg = DecTotal/DecDays

    outfile.write('January, ' + format(JanAvg,'.2f') + '\n')
    outfile.write('February, ' + format(FebAvg,'.2f') + '\n')
    outfile.write('March, ' + format(MarAvg,'.2f') + '\n')
    outfile.write('April, ' + format(AprAvg,'.2f') + '\n')
    outfile.write('May, ' + format(MayAvg,'.2f') + '\n')
    outfile.write('June, ' + format(JuneAvg,'.2f') + '\n')
    outfile.write('July, ' + format(JulyAvg,'.2f') + '\n')
    outfile.write('August, ' + format(AugAvg,'.2f') + '\n')
    outfile.write('September, ' + format(SepAvg,'.2f') + '\n')
    outfile.write('October, ' + format(OctAvg,'.2f') + '\n')
    outfile.write('November, ' + format(NovAvg,'.2f') + '\n')
    outfile.write('December, ' + format(DecAvg,'.2f'))

        
main()



