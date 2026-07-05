import time
class Twitter:

    def __init__(self):
        # we need to maintain:
        # the follower relationships
        # for each user, a heap of their posts
        # to gather the news feed: get the 10 most recent posts
        # of any of that user's followed accounts OR that user account
        # simple: maintain a map of accounts that a user follows
        # and keep a stack of posts for each account
        self.user_follow_map = {}
        self.acct_post_stacks = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.acct_post_stacks:
            self.acct_post_stacks[userId] = []
        self.acct_post_stacks[userId].append((self.counter, tweetId))
        self.counter += 1

    def _get_posts_for_news_feed(self, userId: int):
        # Returns the list of account Ids that should be checked for posts
        # when generating the news feed for `userId`.
        # Takes care of the fact that news feed should include the user's own posts
        posts = []
        ids = self.user_follow_map.get(userId, set()) | {userId}
        for id_ in ids:
            stack_of_posts = self.acct_post_stacks.get(id_)
            if stack_of_posts:
                posts.append(stack_of_posts)
        return posts


    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        max_posts = 10
        # gets the post stacks from all the followed accounts
        # possible_posts = [
        #     self.acct_post_stacks[id_] for id_ in 
        #     self.user_follow_map.get(userId, set())
        #     if id_ in self.acct_post_stacks
        # ]
        possible_posts = self._get_posts_for_news_feed(userId)
        for i, p in enumerate(possible_posts):
            print(f'stack {i}: {len(p)}')
        print()
        # keep track of backwards pointers for all stacks
        stack_idxs = [0 for _ in range(len(possible_posts))]
        stacks_exhausted = set()
        all_read = False
        while len(news_feed) < max_posts and not all_read:
            stack_id = None
            latest_ts = -1
            most_recent_post = None
            
            if len(stacks_exhausted) == len(possible_posts):
                all_read = True

            for stack_num, ptr_into_stack in enumerate(stack_idxs):
                # check if this stack has already been exhausted
                if ptr_into_stack >= len(possible_posts[stack_num]):
                    stacks_exhausted.add(stack_num)
                
                if stack_num in stacks_exhausted:
                    continue

                the_stack = possible_posts[stack_num]
                post_ts, post_id = the_stack[len(the_stack) - 1 - ptr_into_stack]
                if post_ts > latest_ts:
                    latest_ts = post_ts
                    most_recent_post = post_id
                    stack_id = stack_num
            if stack_id is not None:
                stack_idxs[stack_id] += 1
                news_feed.append(most_recent_post)
        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.user_follow_map:
            self.user_follow_map[followerId] = set()
        self.user_follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # TODO: how to handle calls of `unfollow` where the follow relationship didn't exist in the first place
        followed_set = self.user_follow_map.get(followerId)
        if followed_set and followeeId in followed_set:
            followed_set.remove(followeeId)
