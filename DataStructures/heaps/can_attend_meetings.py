"""
https://leetcode.com/problems/meeting-rooms/solution/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

TC:O(nlogn)
SC:O(1)
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if not intervals:
            return True
        
        intervals.sort(key = lambda x: x[0])
        
        j=0
        
        for i in range(len(intervals)-1):
            j=i+1
            if intervals[i][1] > intervals[j][0]:
                return False
        
        return True
        
