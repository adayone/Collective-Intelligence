def kcluster(rows, distance=pearson, k=4):
    #determine the minimum and maxmum values for each point
    ranges = [ ( min([row[i] for row in rows]), max(row[i] for row in rows) ) for i in range(len(rows[0]))]

    # create k random placed centroids
    clusters=[[random.random()*(ranges[i][1] - ranges[i][0]) + ranges[i][0]
        for i in range(len(rows[0]))] for j in range(k)]

    lastmatches=None
    for t in range(100):
        print 'Iteration %d'%t
        bestmatches=[[] for i in range(k)]

        #find which centroid is the closest for each row
        for j in range(len(rows)):
            row=rows[j]
            bestmatch=0
            for i in range(k):
                d=distance(clusters[i], row)
            if d<distance(clusters[bestmatch], row): bestmatch=i
        bestmatches[bestmatch].append(j)

    #If the resulkt are the same as last time, this is complete
    if bestmatches == lastmatches: break
    lastmatches = bestmatches


