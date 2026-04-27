import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) 
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Store: count, tweetId, followeeId, and the index of the NEXT tweet to get
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # 3. Pull the top 10 from the heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If this user has more tweets, push the next one into the heap
            if idx >= 0:
                next_count, next_tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [next_count, next_tweetId, followeeId, idx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)
        
