# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from sunpy.time import parse_time

class TimeSuite:
    """
    An example benchmark that times the performance of sunpy.parse_time()
    function
    """
    def time_parse_time(self):
       t = parse_time('1995-12-31 23:59:60')
       t1 = t5 = parse_time((2001, 1, 1, 12, 12, 12, 8899))

class MemSuite:
    def mem_parse_time(self):
        t = parse_time('1995-12-31 23:59:60')
        return t

class PeakMemorySuite:
    def peakmem_parse_time(self):
        t = parse_time('1995-12-31 23:59:60')