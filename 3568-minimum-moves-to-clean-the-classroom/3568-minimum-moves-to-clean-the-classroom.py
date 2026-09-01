class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litterMap = {}
        startRow = startCol = -1
        litterIndex = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    startRow, startCol = i, j
                elif classroom[i][j] == 'L':
                    litterMap[(i, j)] = litterIndex
                    litterIndex += 1

        totalLitter = len(litterMap)
        if totalLitter == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        heap = []
        heapq.heappush(heap, (0, startRow, startCol, energy, 0))
        visited = {}

        while heap:
            moves, x, y, energyLeft, mask = heapq.heappop(heap)

            if mask == (1 << totalLitter) - 1:
                return moves

            stateKey = (x, y, mask)
            if stateKey in visited and visited[stateKey] >= energyLeft:
                continue
            visited[stateKey] = energyLeft

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                cell = classroom[nx][ny]
                if cell == 'X':
                    continue

                if energyLeft == 0:
                    continue

                nextEnergy = energy if cell == 'R' else energyLeft - 1
                if nextEnergy < 0:
                    continue

                nextMask = mask
                if cell == 'L' and (nx, ny) in litterMap:
                    nextMask |= (1 << litterMap[(nx, ny)])

                heapq.heappush(heap, (moves + 1, nx, ny, nextEnergy, nextMask))

        return -1