
import unittest

TEST_FILE = "testdata/Results_25554.txt"
class Tests(unittest.TestCase):
    def test_loadData_gets_some_data(self):
        import data_reduction
        data = data_reduction.loadData(open(TEST_FILE, 'rb'))
        self.failUnless(data)
    
    def test_transpose_data(self):
        import data_reduction
        data = data_reduction.loadData(open(TEST_FILE, 'rb'))
        self.failUnless(data)
        transposed = data_reduction.transposeData("123123", data)
        self.failUnless(transposed)
        self.assertEqual(2, len(transposed))
        self.assertEqual(32, len(transposed[0]))
        self.assertEqual(32, len(transposed[1]))
        self.assertEqual(transposed[0], ['file', 'sample', '208Pb/206Pb raw              ', 'internal precision', '207Pb/206Pb raw              ', 'internal precision', '205Tl/203Tl  raw             ', 'internal precision', 'beta Tl 5/3                  ', 'internal precision', 'beta Pb 8/6                  ', 'internal precision', '208Pb/206Pb 5/3 exp          ', 'internal precision', '207Pb/206Pb 5/3 exp          ', 'internal precision', '206Pb/204Pb 5/3 exp Hg corr  ', 'internal precision', '207Pb/204Pb 5/3 exp Hg corr  ', 'internal precision', '208Pb/204Pb 5/3 exp Hg corr  ', 'internal precision', '205Tl/203Tl 8/6 exp          ', 'internal precision', 'Total Pb Ion Beam            ', 'internal precision', 'Total Tl Ion Beam            ', 'internal precision', '208Pb Ion Beam               ', 'internal precision', '205Tl Ion Beam               ', 'internal precision'])
        self.assertEqual(transposed[1], ['123123', '', 2.213498, 4.47e-05, 0.9245091, 1.64e-05, 2.43995, 8.87e-05, -2.213926, 0.0037, -2.160808, 0.00209, 2.166547, 6.64e-05, 0.9146257, 1.72e-05, 16.93589, 0.00136, 15.48984, 0.00136, 36.69169, 0.0037, 2.3888, 7.42e-05, 3.111097, 0.00776, 0.9606547, 0.00231, 1.641255, 0.00409, 0.6813918, 0.00164])


