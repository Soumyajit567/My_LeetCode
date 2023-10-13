class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Step 1: Create the graph and in-degree array
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(1, n + 1)}
        
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        
        # Step 2: Queue for courses that can be taken immediately
        queue = deque()
        for course in in_degree:
            if in_degree[course] == 0:
                queue.append(course)
        
        # Time to complete each course (initially it's the duration of each course itself)
        completion_time = [0] + time
        
        # Step 3: Process the courses
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # The time to start a course is the max of the current recorded time and the completion time of its prerequisite
                completion_time[neighbor] = max(completion_time[neighbor], completion_time[course] + time[neighbor - 1])
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # The result is the maximum completion time
        return max(completion_time)