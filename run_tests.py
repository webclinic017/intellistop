from test import test_1, test_time_series
from test.utils import plot
import numpy as np

# test_1.test_iterative("VTI", 15.35)
# test_1.test_iterative("VGT", 18.35)
# test_1.test_iterative("VHT", 13.92)

# differences = []
# differences.append(test_1.test_iterative2("VTI", 15.35))
# differences.append(test_1.test_iterative2("VGT", 18.35))
# differences.append(test_1.test_iterative2("VHT", 13.92))
# differences.append(test_1.test_iterative2("VNQ", 16.81))
# differences.append(test_1.test_iterative2("SPY", 14.44))
# differences.append(test_1.test_iterative2("VO", 15.12))

# transposed = [[] for _ in range(len(differences[0]))]
# for diff_row in differences:
#     for i, diff_val in enumerate(diff_row):
#         transposed[i].append(diff_val)

# variances = [np.var(transpo) for transpo in transposed]

# performance = test_1.reveal_performance(variances)
# print("\r\nPerformance:\r\n")
# for perf in performance:
#     print(f"{perf[0]} : {perf[1]}")
# print("")

test_time_series.test_ts_1()