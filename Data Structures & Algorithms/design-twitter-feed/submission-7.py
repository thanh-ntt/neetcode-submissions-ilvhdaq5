from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # userId -> [(tweetId, time)]
        self.follows = defaultdict(list) # userId -> [userId]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        nf = self.tweets[userId][:]
        for followee in self.follows[userId]:
            nf.extend(self.tweets[followee])
        sorted_nf = sorted(nf, key=lambda a: a[1], reverse=True)[:10]
        return [a[0] for a in sorted_nf]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
