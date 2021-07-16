# DFS(Depth-First Search)

- DFS는 깊이우선 탐색이라고도 부르면 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
- DFS는 스택자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 합니다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 이있으면 그 노드를 스택에 넣고 방문 처리합니다. 방문하지 않은 인접노드가 없으면 수택에서 최상단 노드를 꺼냅니다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\dfs 그림.PNG)



![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\dfs 2.PNG)

![dfs3](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\dfs3.PNG)

![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\dfs 4.PNG)

![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\dfs 문제.PNG)





# BFS(Breadth-First Search)

- BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.

- BFS는 큐자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.

  1. 탐색시작 노드를 큐에 삽입하고 방문처리르 합니다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리합니다.
  3.  더 이상 2번의 과정을 수행할 수 없을떄 까지 반복합니다.

  

![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\BFS.PNG)



![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\BFS2.PNG)

![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\BFS3.PNG)

![BFS4](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\BFS4.PNG)



![](C:\Users\user1\Desktop\study_alone\최적의 코딩을 결정하는 기본 알고리즘\BFS 코드.PNG)



