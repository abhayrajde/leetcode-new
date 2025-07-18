class Twitter:

    def __init__(self):
        self.timerCount = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timerCount, tweetId])
        self.timerCount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        latestTweets = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                timerCount, tweetId = self.tweetMap[followeeId][index]
                latestTweets.append([timerCount, tweetId, followeeId, index - 1])
        
        heapq.heapify(latestTweets)
        while latestTweets and len(res) < 10:
            timerCount, tweetId, followeeId, index = heapq.heappop(latestTweets)
            
            res.append(tweetId)
            if index >= 0:
                timerCount, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(latestTweets, [timerCount, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
