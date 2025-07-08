from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])          # 격자 크기 (행, 열)
    
    # 1) 네 방향 이동 좌표 (상·하·좌·우)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 2) BFS 큐: (행, 열, 지금까지 걸음 수)
    q = deque([(0, 0, 1)])
    
    # 3) 방문 처리 배열 (n×m) — 시작점은 이미 방문
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    # 4) 큐가 빌 때까지 반복
    while q:
        x, y, dist = q.popleft()
        
        # 5) 목표 지점에 도착했으면 최단 거리 return
        if x == n-1 and y == m-1:
            return dist
        
        # 6) 네 방향 탐색
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            # 7) 격자 내부 & 길(1) & 미방문이면 방문하기
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    
    # 8) 목표에 도달 못했으면 -1
    return -1
