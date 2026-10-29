import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.t))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        feed = []
        self.follows[userId].add(userId)

        for followee in self.follows[userId]:
            if followee in self.posts:
                idx = len(self.posts[followee]) - 1
                tweetId, t = self.posts[followee][idx]
                heapq.heappush(min_heap, (t, tweetId, followee, idx - 1))

        while min_heap and len(feed) < 10:
            t, tweetId, followee, idx = heapq.heappop(min_heap)
            feed.append(tweetId)
            if idx >= 0:
                tweetId, t = self.posts[followee][idx]
                heapq.heappush(min_heap, (t, tweetId, followee, idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
