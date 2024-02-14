import numpy as np

def outlier_counter_three_SD(array):
    """Return number of outliers from a numpy array."""
    mean = np.mean(array)
    std = np.std(array)
    n_outlier = 0
    population = len(array)
    LTSmean = mean - (std * 1)
    UTSmean = mean + (std * 1)
    # print(LTSmean, UTSmean)
    for case in array: 
        if case < LTSmean or case > UTSmean:
            n_outlier = n_outlier + 1
    # print(LTSmean, UTSmean)
    return(n_outlier)

def outlier_whiskers(array):
    """Return number of outliers from a numpy array."""
    mean = np.mean(array)
    std = np.std(array)
    n_outlier = 0
    population = len(array)
    Q1 = np.quantile(array, 0.25)
    Q3 = np.quantile(array, 0.75)
    IQR = Q3 - Q1
    Lbound = Q1 - 1.5 * IQR
    Ubound = Q3 + 1.5 * IQR
    # print(LTSmean, UTSmean)
    for case in array: 
        if case < Lbound or case > Ubound:
            n_outlier = n_outlier + 1
    # print(LTSmean, UTSmean)
    return(n_outlier)

def coefficient_of_range(array):
    """Calculate the coefficient of range of a numpy array."""
    highest_number = max(array)
    smallest_number = min(array)
    coef_range = (highest_number - smallest_number) / (highest_number + smallest_number)
    return coef_range

def coefficient_of_dispersion(array):
    """Calculate the coefficient of dispersion of a numpy array."""
    median = np.median(array)
    suma = 0
    count_n = len(array)
    for x in array:
        temp = abs(x - median)
        suma = suma + temp
    coefficient_of_dispersion = suma / (median * count_n)
    return coefficient_of_dispersion

def coefficient_of_mean_deviation(array):
    """Calculate the coefficient of mean deviation from a numpy array."""
    # based on bottom eq: https://www.cuemath.com/data/measures-of-dispersion/
    # from: https://www.knowledgehut.com/blog/data-science/dispersion-in-statistics
    # from: https://www.economicsdiscussion.net/mean-deviation/mean-deviation-coefficient-of-mean-deviation/2547
    mean = np.mean(array)
    count_n = len(array)
    temp = 0
    suma = 0
    for x in array:
        temp = abs(x - mean)
        suma = suma + temp
    coefficient_of_mean_deviation = suma / (count_n * mean)
    return coefficient_of_mean_deviation  

def coefficient_of_inner_quantile_range_ninety(array):
    """Calculate coefficient inner quantile range of 90 percent of a numpy array."""
    # based on bottom eq: https://www.cuemath.com/data/measures-of-dispersion/
    # from: https://www.knowledgehut.com/blog/data-science/dispersion-in-statistics
    Q005 = np.quantile(array, 0.05)
    Q95 = np.quantile(array, 0.95)
    return ((Q95 - Q005) / (Q95 + Q005)) #Koeficient of IQR
    

def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # GITHUB link https://github.com/oliviaguest/gini
    # array = array.flatten() #all values are treated equally, arrays must be 1d
    if np.amin(array) < 0:
        array -= np.amin(array) #values cannot be negative
    array += 0.0000001 #values cannot be 0
    array = np.sort(array) #values must be sorted
    index = np.arange(1,array.shape[0]+1) #index per array element
    n = array.shape[0]#number of array elements
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array))) #Gini coefficient


def outlier_one_sigma(array):
    """Calculate number of outliers in certain range of std from a numpy array"""
    mean = np.mean(array)
    std = np.std(array)
    n_outlier = 0
    population_n = len(array)
    LTSmean = mean - (std * 1)
    UTSmean = mean + (std * 1)
    # print(LTSmean, UTSmean)
    for case in array: 
        if case < LTSmean or case > UTSmean:
            n_outlier = n_outlier + 1
    # print(LTSmean, UTSmean)
    outlier_one_sigma = n_outlier / population_n
    return(outlier_one_sigma)