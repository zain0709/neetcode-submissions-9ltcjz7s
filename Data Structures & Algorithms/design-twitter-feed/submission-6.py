import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.counts = 0
        self.tweetMap = defaultdict(list)
        self.followerMap = defaultdict(list)
        self.queue = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.followerMap[userId]:
            self.followerMap[userId] = [userId]
        self.tweetMap[userId].append(tweetId)
        self.counts += 1
        heapq.heappush(self.queue, (-self.counts, (userId, tweetId)))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        test = []
        temp = []
        while self.queue and len(test) < 10:
            item = heapq.heappop(self.queue)
            temp.append(item)
            uid = item[1][0]
            tid = item[1][1]
            if uid in self.followerMap[userId]:
                test.append(tid)
        for item in temp:
            heapq.heappush(self.queue, item)
        return test

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.followerMap[followerId]:
            self.followerMap[followerId] = [followerId]
        if followeeId not in self.followerMap[followerId]:
            self.followerMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)

