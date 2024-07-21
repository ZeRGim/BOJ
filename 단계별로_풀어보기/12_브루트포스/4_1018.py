N,M=map(int,input().split())
board=[]
cnt=[]
for i in range(N):
    temp=input()
    board.append(temp)
chessboard=[]
for i in range(M-7):
    for k in range(N-7):
        chessboard.append([])
        for j in range(8):
            chessboard[k+i].append(board[j+k][i:i+8])
for i in range(len(chessboard)):
    for j in chessboard[i]:
        if len(chessboard[i]) > 8:
            for k in range(len(chessboard[i])//8):
                chessboard.append(chessboard[i][k*8:(k+1)*8])
            del chessboard[i]

def checkW(board):
    realwchess=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    cnt=0
    for i in range(8):
        for j in range(8):
            if realwchess[i][j] != board[i][j]:
                cnt += 1
    return cnt

def checkB(board):
    realbchess=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    cnt=0
    for i in range(8):
        for j in range(8):
            if realbchess[i][j] != board[i][j]:
                cnt += 1
    return cnt
for i in range(len(chessboard)):
    if chessboard[i]:
        cnt.append(checkB(chessboard[i]))
        cnt.append(checkW(chessboard[i]))
print(min(cnt))