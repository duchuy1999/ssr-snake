#Edit from https://github.com/noahspriggs/battlesnake-python/blob/master/app/AStar.py

import sys

def manhattan_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return list(reversed(total_path))

def neighbors(current, board):
    neighbors_list = []
    if current[0]-1 >= 0 and board[current[0]-1][current[1]] != 0:
        neighbors_list.append((current[0]-1, current[1]))
    if current[0]+1 < len(board[0]) and board[current[0]+1][current[1]] != 0:
        neighbors_list.append((current[0]+1, current[1]))
    if current[1]-1 >= 0 and board[current[0]][current[1]-1] != 0:
        neighbors_list.append((current[0], current[1]-1))
    if current[1]+1 < len(board) and board[current[0]][current[1]+1] != 0:
        neighbors_list.append((current[0], current[1]+1))
    return neighbors_list

def a_star(start, end, board):
    open_list = []
    closed_list = []
    open_list.append(start)
    came_from = {}

    g_score = [[10000 for x in range(len(board[y]))] for y in range(len(board))]
    g_score[start[0]][start[1]] = 0

    f_score = [[10000 for x in range(len(board[y]))] for y in range(len(board))]
    f_score[start[0]][start[1]] = manhattan_dist(start, end)

    while (len(open_list) > 0):
        current = min(open_list, key=lambda p: f_score[p[0]][p[1]])

        if (current == end):
            return reconstruct_path(came_from, end)
    
        open_list.remove(current)
        closed_list.append(current)
        
        for neighbor in neighbors(current, board):
            #print("current:", current)
            #print("neighbor:", neighbor)
            if neighbor in closed_list:
                continue
            temp_g_score = g_score[current[0]][current[1]] + manhattan_dist(current, neighbor)
            if neighbor not in open_list:
                open_list.append(neighbor)
            elif temp_g_score >= g_score[neighbor[0]][neighbor[1]]:
                continue
            
            came_from[neighbor] = current
            g_score[neighbor[0]][neighbor[1]] = temp_g_score
            f_score[neighbor[0]][neighbor[1]] = temp_g_score + manhattan_dist(neighbor, end)

    return None

def main():
    #a_star((4,4), (4,0), [[1,1,1,0,1], [0,0,1,0,0], [1,1,1,0,0],[0,0,1,1,1],[1,1,1,1,1]])
    return

main()














"""import heapq

EMPTY = 0
FOOD = 1
BODY = 2

class Cell:
    def __init__ (x, y, status):
        self.x = x
        self.y = y
        self.status = status
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None
        self.neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    
    def __lt__(self, other):
        return self.f < other.f
    
    
    def setValues(parent, end):
        self.parent = parent
        self.g = parent.g + 1
        self.f = self.g + self.h
        self.h = abs(self.x - end[0]) +  abs(self.y - end[1]) #Manhattan distance as heuristics
        
    def getParent():
        return self.parent
        

def astar(board, start, end):
    #start, end should be a tuple (x, y) 
      
    open_list = []
    closed_list = []
    headCell = Cell(start[0], start[1], end)
    endCell = None
    open_list.append(headCell)
    heapq.heapify(open_list)
    
    while len(open_list) != 0:
        parent = heapq.heappop(open_list)
        #initiate 4 adjacent cells
        
        for neighbor in parent.neighbors:
            if neighbor == end:
                endCell = Cell(neighbor[0], neighbor[1], end)
                endCell.setValues(parent)
           
       
        leftCell = Cell(start[0]-1, start[1], end)
        rightCell = Cell(start[0]+1, start[1], end)
        upCell = Cell(start[0], start[1]-1, end)
        downCell = Cell(start[0], start[1]+1, end)
        
        leftCell.setValues(parent)
        rightCell.setValues(parent)
        upCell.setValues(parent)
        downCell.setValues(parent)
        
        successors[]
        successors.append(leftCell)
        successors.append(rightCell)
        successors.append(upCell)
        successors.append(downCell)
        
        for successor in successors:
            if successor.x == end[0] and successor.y == end[1]:
                #found the food
        """