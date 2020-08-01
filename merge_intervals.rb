# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    return [] if intervals.empty?
    intervals = intervals.sort do |interval1, interval2|
        if interval1[0] < interval2[0]
            -1
        elsif interval1[0] > interval2[0]
            1
        else
            interval1[1] <=> interval2[1]
        end
    end

    merged_intervals = []
    leftBound, rightBound = intervals[0][0], intervals[0][1]

    (1...intervals.length).each do |idx|
        interval = intervals[idx]
        if interval[0] > rightBound
            merged_intervals << [leftBound, rightBound]
            leftBound, rightBound = interval[0], interval[1]
            next
        end

        # interval left <= right, expand right
        rightBound = interval[1] > rightBound ? interval[1] : rightBound
    end
    merged_intervals << [leftBound, rightBound]

    merged_intervals
end

p merge([[1,4],[4,5]])