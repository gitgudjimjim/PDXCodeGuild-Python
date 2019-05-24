# lab_18_peaks_and_valleys
def peaks(data):
#    """
#    Returns the indices of peaks. A peak has a lower number on both the left and the right.
#    """
#    data = []


    peaks = []
    for i in range(1, (len(data)-1):
        left = data[i-1]
        mid = data[i]
        right = data[i+1]
        if left < mid > right:
            peaks.append(i)
            return print(peaks)

data = ['1', '2', '3', '4', '5', '6', '7', '6', '5', '4', '5', '6', '7', '8' , '9' , '8' , '7', '6','7', '8']
#peaks(data)
