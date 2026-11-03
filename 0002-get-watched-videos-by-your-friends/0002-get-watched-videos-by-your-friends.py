from collections import deque, Counter
from typing import List

class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        """
        Find videos watched by friends at a specific friendship level.
      
        Args:
            watchedVideos: List where watchedVideos[i] contains videos watched by person i
            friends: List where friends[i] contains the friend IDs of person i
            id: Starting person's ID
            level: The friendship level to search (1 = direct friends, 2 = friends of friends, etc.)
      
        Returns:
            List of videos sorted by frequency (ascending) and then alphabetically
        """
        # Initialize BFS queue with starting person
        queue = deque([id])
        # Track visited people to avoid cycles
        visited = {id}
      
        # Perform BFS to reach the target friendship level
        for _ in range(level):
            # Process all people at current level
            current_level_size = len(queue)
            for _ in range(current_level_size):
                current_person = queue.popleft()
                # Add unvisited friends to the queue for next level
                for friend_id in friends[current_person]:
                    if friend_id not in visited:
                        visited.add(friend_id)
                        queue.append(friend_id)
      
        # Count videos watched by all people at the target level
        video_count = Counter()
        for person_id in queue:
            for video in watchedVideos[person_id]:
                video_count[video] += 1
      
        # Sort videos by frequency (ascending), then alphabetically
        return sorted(video_count.keys(), key=lambda video: (video_count[video], video))
