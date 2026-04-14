class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.ts))
        self.ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        nf = list(self.posts[userId])
        for followee in self.follows[userId]:
            nf.extend(self.posts[followee])
        nf.sort(key=lambda t: t[1], reverse=True)
        return [t[0] for t in nf][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
        
