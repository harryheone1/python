"""
this function try to check sample stability per attribute by distribution entropy

input: 
    groupFrameName is the resample rate, such as '1H', '30s' and so on
    dfInput is the input dataframe (pandas dataframe)
    attrToPlot is the attribute considered

output:
    entropy plots
""" 



from scipy.stats import entropy
def Plot_Entryopy_New_Vals( groupFrameName,dfInput,attrToPlot):
    valNumList = []
    timeDayVals = dfInput.resample(groupFrameName).sum().index.values
    entropyList = []
    maxNumVariety = 0 
    newValsTimeList = []
    
    for i in range( len(timeDayVals) ):
        if i%50 ==0:
            print(str(i)+'/'+str(len(timeDayVals)) )
        thisDayTime = timeDayVals[i]
        normProbArray = dfInput.loc[:thisDayTime][attrToPlot].value_counts(normalize=True).tolist()
        entropyList.append( entropy(normProbArray ) )
        if maxNumVariety < len(normProbArray):
            maxNumVariety = len(normProbArray)
            newValsTimeList.append(thisDayTime )   
    entropyTimeSeries = pd.Series(index=timeDayVals,data = entropyList )


    fig,ax = plt.subplots(figsize=(10,5) )
    entropyTimeSeries.plot()
    for i in range(len(newValsTimeList )):
        ax.axvline(pd.to_datetime( newValsTimeList[i]),color = 'r',linestyle='--' )
    ax.set_title(attrToPlot)
    plt.show()
