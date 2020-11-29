def solution(m, n, board):
    
    matched = True
    while matched:
        matched = []
        for i in range(m): # m => 높이
            for j in range(n): # n => 폭
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '#':
                    matched.append([i, j])
    
		for i, j in matched:
			board[i][j] = board[i+1][j] = board[i][j+1] = board[i+1][j+1] = '#'
	
		for _ in range(m):  
			for i in range(m-1):
				for j in range(n):
					if board[i+1][j] == '#':
						board[i+1][j], board[i][j] = board[i][j], '#'
    return