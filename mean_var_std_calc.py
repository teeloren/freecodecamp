import numpy as np


def calculate(list):
    # len_list = len(list)
    # if len_list != 9:
    #     return  "List must contain nine numbers."
    # else:
    try:
        arr = np.array(list)  # flatten matrix
        mtx = arr.reshape(3, 3)  # 3x3 matrix
        calculations = dict()

        # along both axes and for the flattened matrix
        # mean
        axis1 = np.mean(mtx, axis=0)
        axis2 = np.mean(mtx, axis=1)
        flattened = np.mean(arr)

        # dictionary containing the mean,
        calculations.setdefault('mean', [[*axis1], [*axis2], flattened])

        # variance, standard deviation, max, min, and sum
        axis1 = np.var(mtx, axis=0)
        axis2 = np.var(mtx, axis=1)
        flattened = np.var(arr)
        calculations.setdefault('variance', [[*axis1], [*axis2], flattened])

        axis1 = np.std(mtx, axis=0)
        axis2 = np.std(mtx, axis=1)
        flattened = np.std(arr)
        calculations.setdefault('standard deviation', [
                                [*axis1], [*axis2], flattened])

        axis1 = np.max(mtx, axis=0)
        axis2 = np.max(mtx, axis=1)
        flattened = np.max(arr)
        calculations.setdefault('max', [[*axis1], [*axis2], flattened])

        axis1 = np.min(mtx, axis=0)
        axis2 = np.min(mtx, axis=1)
        flattened = np.min(arr)
        calculations.setdefault('min', [[*axis1], [*axis2], flattened])

        axis1 = np.sum(mtx, axis=0)
        axis2 = np.sum(mtx, axis=1)
        flattened = np.sum(arr)
        calculations.setdefault('sum', [[*axis1], [*axis2], flattened])
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    return calculations


list = [0, 1, 2,  5, 6, 7, 8]
print(calculate(list))
