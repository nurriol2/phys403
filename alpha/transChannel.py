def peaks(channelDictionary):

    maximumCount = max(channelDictionary.values())

    channelNumber = [channel for channel, count in channelDictionary.items() if count == maximumCount]

    return channelNumber
