#code
a =[[1,2,3,4,5],[6,7,8,9,12]]
print(a[7][2])
print(a)

rr = (-1,-1,-1, 0, 0, 1, 1, 1)
cc = (-1, 0, 1,-1, 1,-1, 0, 1)

def isValid(r,c,R,C):
    return r>=0 and c>=0 and r<R and c<C

def DFS( grid, r, c, R, C, spiritual):
    spiritual[r][c] = False
    ret = 1
    
    for i in range(8):
        newR = r + rr[i]
        newC = c + cc[i]
        if isValid(newR, newC, R, C) and spiritual[newR][newC]:
            ret += DFS( grid, newR, newC, R, C, spiritual )
    
    return ret

def maxCities(grid,n,m):
    spiritual = [ [ False for _ in range(m) ] for _ in range(n) ]
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '*':
                for i in range(8):
                    newR = r + rr[i]
                    newC = c + cc[i]
                    if isValid(newR, newC, n, m) and grid[newR][newC]=='.':
                        spiritual[newR][newC] = True
    
    ret = 0
    for r in range(n):
        for c in range(m):
            if spiritual[r][c]:
                ret = max( ret, DFS( grid,r,c,n,m,spiritual ) )
    
    return ret

