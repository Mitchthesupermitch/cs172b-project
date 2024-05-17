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
