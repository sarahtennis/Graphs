### 3. Questions
##### 1. To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?

The number of times to call addFriendship() would be 500 = (100 * 10) / 2.
To have an average of 10 friends for each user, there would need to be 1,000 total friends across all users.
The addFriendship() method creates 2 friends every call, so 1,000 / 2 = 500 total calls.

##### 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?

### 4. Stretch Goal
##### 1. You might have found the results from question #2 above to be surprising. Would you expect results like this in real life? If not, what are some ways you could improve your friendship distribution model for more realistic results?
Unsure how to mathematically solve #2 above, but an improvement on the distribution model would be to use weighted friendships. Realistically, friendships are not distributed randomly and are strongly influenced by many factors. Assuming no geographical/social/etc information is known, the model can be improved upon by increasing the likelihood of forming a connection with someone if you share a common friend (ex. if you have a common friend with a user, create a range for that user to check a randomized number against instead of a single integer).

##### 2. If you followed the hints for part 1, your populateGraph() will run in O(n^2) time. Refactor your code to run in O(n) time. Are there any tradeoffs that come with this implementation?
After refactoring the populateGraph() method, the best case runtime is O(n). BUT, though unlikely, the worst case runtime would potentially be O(infinity) -- in the case that enough unique random friend pairs are never generated to reach the necessary average. As either the total number of users and/or the desired average number of friends increase, the probability of observing an O(n) runtime also increases as it is less likely that friend pairs will be duplicated.