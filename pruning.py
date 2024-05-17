def removeChestLabels(stuff, indexes ):
    '''stuff: original dictionary from the pickl file
        indexes: List of indexes to remove'''
    removing = []
    for i in indexes:
        removing.append(np.where(stuff['label'] == i)[0])

    removes = np.unique(np.concatenate(removing))
    stuff['label'] = np.delete(stuff['label'],removes)
    stuff['signal']['chest']['ACC'] = np.delete(stuff['signal']['chest']['ACC'],removes,axis=0)
    stuff['signal']['chest']['ECG'] = np.delete(stuff['signal']['chest']['ECG'],removes,axis=0)
    stuff['signal']['chest']['EMG'] = np.delete(stuff['signal']['chest']['EMG'],removes,axis=0)
    stuff['signal']['chest']['EDA'] = np.delete(stuff['signal']['chest']['EDA'],removes,axis=0)
    stuff['signal']['chest']['Temp'] = np.delete(stuff['signal']['chest']['Temp'],removes,axis=0)
    stuff['signal']['chest']['Resp'] = np.delete(stuff['signal']['chest']['Resp'],removes,axis=0)

    return stuff

def removeLabels(stuff, indexes):
    '''stuff: original dictionary from the pickl file
        indexes: List of indexes to remove
        This removes the associated data from both the  wrist and chest.
        This will expand the wrist data to be the same length as the labels'''
    stuff = expandWrists(stuff)

    
    removing = []
    for i in indexes:
        removing.append(np.where(stuff['label'] == i)[0])

    removes = np.unique(np.concatenate(removing))
    stuff['label'] = np.delete(stuff['label'],removes)
    stuff['signal']['chest']['ACC'] = np.delete(stuff['signal']['chest']['ACC'],removes,axis=0)
    stuff['signal']['chest']['ECG'] = np.delete(stuff['signal']['chest']['ECG'],removes,axis=0)
    stuff['signal']['chest']['EMG'] = np.delete(stuff['signal']['chest']['EMG'],removes,axis=0)
    stuff['signal']['chest']['EDA'] = np.delete(stuff['signal']['chest']['EDA'],removes,axis=0)
    stuff['signal']['chest']['Temp'] = np.delete(stuff['signal']['chest']['Temp'],removes,axis=0)
    stuff['signal']['chest']['Resp'] = np.delete(stuff['signal']['chest']['Resp'],removes,axis=0)

    stuff['signal']['wrist']['ACC'] = np.delete(stuff['signal']['wrist']['ACC'],removes,axis=0)
    stuff['signal']['wrist']['BVP'] = np.delete(stuff['signal']['wrist']['BVP'],removes,axis=0)
    stuff['signal']['wrist']['EDA'] = np.delete(stuff['signal']['wrist']['EDA'],removes,axis=0)
    stuff['signal']['wrist']['TEMP'] = np.delete(stuff['signal']['wrist']['TEMP'],removes,axis=0)

    return stuff

def expandWrists(stuff):
    '''This will expand the wrist data to be the same length in axis 0 as the labels
    IMPORTANT: assumes that data points are not changed until the next measurement'''

    
    multiplier = np.ceil(len(stuff['label']) / len(stuff['signal']['wrist']['ACC']))
    cutback = len(stuff['label']) % len(stuff['signal']['wrist']['ACC'])
    stuff['signal']['wrist']['ACC'] = np.repeat(stuff['signal']['wrist']['ACC'], multiplier ,axis=0)[:-(len(stuff['signal']['wrist']['ACC'])-cutback)] if cutback > 0\
                                      else np.repeat(stuff['signal']['wrist']['ACC'], multiplier ,axis=0)

    
    multiplier = np.ceil(len(stuff['label']) / len(stuff['signal']['wrist']['BVP']))
    cutback = len(stuff['label']) % len(stuff['signal']['wrist']['BVP'])
    stuff['signal']['wrist']['BVP'] = np.repeat(stuff['signal']['wrist']['BVP'], multiplier ,axis=0)[:-(len(stuff['signal']['wrist']['BVP'])-cutback)] if cutback > 0 \
                                      else np.repeat(stuff['signal']['wrist']['BVP'], multiplier ,axis=0)


    multiplier = np.ceil(len(stuff['label']) / len(stuff['signal']['wrist']['EDA']))
    cutback = len(stuff['label']) % len(stuff['signal']['wrist']['EDA'])
    stuff['signal']['wrist']['EDA'] = np.repeat(stuff['signal']['wrist']['EDA'], multiplier ,axis=0)[:-(len(stuff['signal']['wrist']['EDA'])-cutback)] if cutback > 0\
                                      else np.repeat(stuff['signal']['wrist']['EDA'], multiplier ,axis=0)


    multiplier = np.ceil(len(stuff['label']) / len(stuff['signal']['wrist']['TEMP']))
    cutback = len(stuff['label']) % len(stuff['signal']['wrist']['TEMP'])
    stuff['signal']['wrist']['TEMP'] = np.repeat(stuff['signal']['wrist']['TEMP'], multiplier ,axis=0)[:-(len(stuff['signal']['wrist']['TEMP'])-cutback)] if cutback > 0\
                                       else np.repeat(stuff['signal']['wrist']['TEMP'], multiplier ,axis=0)

    return stuff
