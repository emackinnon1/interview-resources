# 16.3 Tasks Scheduling (medium)

#### Problem Statement  <a href="#problem-statement" id="problem-statement"></a>

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

**Example 1:**

```
Input:  
    Tasks=3, 
    Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. 
Similarly, task '1' needs to finish before '2' can be scheduled. 
A possible sceduling of tasks is: [0, 1, 2] 
```

**Example 2:**

```
Input: 
    Tasks=3, 
    Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, 
therefore they cannot be sceduled.
```

**Example 3:**

```
Input: 
    Tasks=6, 
    Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible sceduling of tasks is: [0 1 4 3 2 5] 
```

### Solution

```java
public static boolean isSchedulingPossible(int tasks, int[][] prerequisites) {
        List<Integer> res = new ArrayList<>();
        // 1. Initialize the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> indegree = new HashMap<>();

        for (int i = 0; i < tasks; i++) {
            graph.put(i, new ArrayList<>());
            indegree.put(i, 0);
        }

        // 2. Build the graph
        for (int i = 0; i < prerequisites.length; i++) {
            int start = prerequisites[i][0], end = prerequisites[i][1];
            graph.get(start).add(end);
            indegree.put(end, indegree.get(end) + 1);
        }

        // 3. Add all the sources(i.e., vertices with in-degree 0)
        Queue<Integer> sources = new LinkedList<>();
        for (Map.Entry<Integer, Integer> entry : indegree.entrySet()) {
            if (entry.getValue() == 0)
                sources.offer(entry.getKey());
        }
        // 4. Process the sources and add it to the result, decrement the in-degree by
        // one of all the children
        while (!sources.isEmpty()) {
            int vertex = sources.poll();
            res.add(vertex);
            for (int child : graph.get(vertex)) {
                indegree.put(child, indegree.get(child) - 1);
                if (indegree.get(child) == 0)
                    sources.add(child);
            }
        }
        // if res doesn't contain all tasks, there is a cyclic dependency
        // between tasks, therefore, we
        // will not be able to schedule all tasks
        return res.size() == tasks;
    }

```

**Time complexity**&#x20;

In step ‘4’, each task can become a source only once and each edge (prerequisite) will be accessed and removed once. Therefore, the time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites.

**Space complexity**&#x20;

The space complexity will be O(V+E), ), since we are storing all of the prerequisites for each task in an adjacency list.
