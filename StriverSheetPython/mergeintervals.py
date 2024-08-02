class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        nintervals=[intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0]<=nintervals[-1][1]:
                nintervals[-1][1]=max(nintervals[-1][1],intervals[i][1])
            else:
                nintervals.append(intervals[i])
        return nintervals
