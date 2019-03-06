import random
from stack import Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships

        ''' ----- LECTURE CODE ----- O(n^2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )
        random.shuffle(possibleFriendships)
        print(possibleFriendships[:20])
        print(len(possibleFriendships))
        '''

        # best case runtime O(n), worst case O(infinity)
        # runtime is closer to O(n) as (numUsers * avgFriendships / 2) approachs infinity
        # smaller probablity of randomly generated duplicates
        friendships = set()
        while len(friendships) < (numUsers * avgFriendships / 2):
            connection = {random.randint(1,numUsers), random.randint(1, numUsers)}
            if len(connection) > 1 and connection not in friendships:
                friendships.add(frozenset(connection))

        for connection in friendships:
            first = 0
            second = 0
            counter = 0
            for id in connection:
                if counter % 2 == 0:
                    first = id
                    counter += 1
                else:
                    second = id
            self.addFriendship(first, second)


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # initialize stack
        s = Stack()
        # start at argument user (put in stack)
        s.push(userID)

        while s.size():
            # pop off stack
            current = s.pop()

            # place self in path
            if current in visited:
                visited[current].append(current)
            else:
                visited[current] = [current]
            
            # look at connections
            for friend in self.friendships[current]:
                # for each connection put key as user, value = path
                if friend not in visited:
                    visited[friend] = list(visited[current])
                    # add to stack, repeat
                    s.push(friend)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
