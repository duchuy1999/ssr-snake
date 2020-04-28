import sys
from astar import a_star

def find_food(board, food_list, head):
    nearest_food = None
    shortest_path = None
    path_length = sys.maxsize

    for food in food_list:

        food_path = a_star(head, food, board)
        if food_path != None and shortest_path == None:
            shortest_path = food_path
            nearest_food = food
        if food_path != None and shortest_path != None and len(shortest_path) > len(food_path):
            shortest_path = food_path
            nearest_food = food
            
        
    if shortest_path != None:
        return shortest_path[1]
    else:
        return None
    
def get_dir(head, neighbor):
    if neighbor[0] == head[0] - 1 and neighbor[1] == head[1]:
        return "left"
    elif neighbor[0] == head[0] + 1 and neighbor[1] == head[1]:
        return "right"
    elif neighbor[0] == head[0] and neighbor[1] == head[1] - 1:
        return "up"
    elif neighbor[0] == head[0] and neighbor[1] == head[1] + 1:
        return "down"
    else:   
        return None
        
def main():
    #board = [[1,1,1,0,1], [0,0,1,0,0], [1,1,1,0,0],[0,0,1,1,1],[1,2,1,1,2]]
    #print(find_food(board, [(4,1),(4,4)], (0,0)))
    return
    
main()