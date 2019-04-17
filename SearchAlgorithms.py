from collections import deque
import math
class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors. parant
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        if self.gOfN < other.gOfN:
            return True
        else:
            return False
def find_min_Heuristic (ls_of_nodes):
    node = ls_of_nodes[0]
    for index in range(len(ls_of_nodes)-1):
        if ls_of_nodes[index].heuristicFn > ls_of_nodes[index+1].heuristicFn:
            node=ls_of_nodes[index+1]
    return node
class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        mazeStr= mazeStr.replace(",","")
        maze_list = mazeStr.split(" ")
        counter=0
        self.start_node_id=-1
        self.goal_node_id=-1
        self.graph={}
        self.xandy={}
        # fill the nodes of the graph
        for row_index in range(len(maze_list)):
            for char_index in range(len(maze_list[row_index])):
                current_char = maze_list[row_index][char_index]
                temp_node = Node(0)
                temp_node.id=counter
                # cheak the right of the node
                if char_index+1 <len(maze_list[row_index]):
                    if maze_list[row_index][char_index+1] !='#':
                        temp_node.right=counter+1
                    else:
                        temp_node.right=-1
                else:
                    temp_node.right=-1
                # cheak the left of the node
                if char_index-1 >=0:
                    if maze_list[row_index][char_index-1] !='#':
                        temp_node.left=counter-1
                    else:
                        temp_node.left = -1
                else:
                    temp_node.left = -1
                # cheak the done node
                if row_index +1 <len(maze_list):
                    if maze_list[row_index+1][char_index] != '#':
                        temp_node.down=counter+len(maze_list[row_index])
                    else:
                        temp_node.down=-1
                else:
                    temp_node.down=-1
                # cheak the up node
                if row_index -1 >=0:
                    if maze_list[row_index-1][char_index] != '#':
                        temp_node.up=counter-len(maze_list[row_index])
                    else:
                        temp_node.up=-1
                else:
                    temp_node.up =-1
                if current_char=='S':
                    self.start_node_id=counter
                elif current_char =='E':
                    self.goal_node_id=counter
                if(edgeCost!=None):
                    temp_node.edgeCost=edgeCost[counter]
                    temp_node.gOfN=math.inf
                    temp_node.heuristicFn=math.inf
                    #print(counter,temp_node.heuristicFn)
                self.graph[counter]=temp_node
                self.xandy[counter]=row_index, char_index
                counter+=1
        #print(self.xandy)
        '''for key , val in self.graph.items():
            print(key,val.right,val.left,val.down,val.up,val.edgeCost)
        print(self.goal_node_id,self.start_node_id)'''

    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        stack=[]
        stack.append(self.start_node_id)
        visited = []
        while stack.__len__() > 0:
            vis_node = stack.pop()
            visited.append(vis_node)
            if vis_node == self.goal_node_id:
                break

            if self.graph[vis_node].left != -1 and not (visited.__contains__(self.graph[vis_node].left)) \
                    and not (stack.__contains__(self.graph[vis_node].left)):
                stack.append(self.graph[vis_node].left)
                self.graph[self.graph[vis_node].left].previousNode = vis_node

            if self.graph[vis_node].right != -1 and not (visited.__contains__(self.graph[vis_node].right)) \
                    and not (stack.__contains__(self.graph[vis_node].right)):
                stack.append(self.graph[vis_node].right)
                self.graph[self.graph[vis_node].right].previousNode = vis_node

            if self.graph[vis_node].down != -1 and not (visited.__contains__(self.graph[vis_node].down)) \
                    and not (stack.__contains__(self.graph[vis_node].down)):
                stack.append(self.graph[vis_node].down)
                self.graph[self.graph[vis_node].down].previousNode = vis_node
            if self.graph[vis_node].up != -1 and not (visited.__contains__(self.graph[vis_node].up)) \
                    and not (stack.__contains__(self.graph[vis_node].up)):
                stack.append(self.graph[vis_node].up)
                self.graph[self.graph[vis_node].up].previousNode = vis_node

        path = []
        n = self.graph[self.goal_node_id].previousNode
        path.append(self.goal_node_id)
        while n != None:
            path.append(n)
            n = self.graph[n].previousNode
        path.reverse()
        self.path = None
        self.fullPath = visited
        return self.path, self.fullPath

    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        queue = deque()
        queue.append(self.start_node_id)
        visited = []
        while queue.__len__() > 0:
            vis_node = queue.popleft()
            visited.append(vis_node)
            if vis_node == self.goal_node_id:
                break
            if self.graph[vis_node].up != -1 and not (visited.__contains__(self.graph[vis_node].up)) \
                    and not (queue.__contains__(self.graph[vis_node].up)):
                queue.append(self.graph[vis_node].up)
                self.graph[self.graph[vis_node].up].previousNode = vis_node

            if self.graph[vis_node].down != -1 and not (visited.__contains__(self.graph[vis_node].down)) \
                    and not (queue.__contains__(self.graph[vis_node].down)):
                queue.append(self.graph[vis_node].down)
                self.graph[self.graph[vis_node].down].previousNode = vis_node

            if self.graph[vis_node].left != -1 and not (visited.__contains__(self.graph[vis_node].left)) \
                    and not (queue.__contains__(self.graph[vis_node].left)):
                queue.append(self.graph[vis_node].left)
                self.graph[self.graph[vis_node].left].previousNode = vis_node

            if self.graph[vis_node].right != -1 and not (visited.__contains__(self.graph[vis_node].right)) \
                    and not (queue.__contains__(self.graph[vis_node].right)):
                queue.append(self.graph[vis_node].right)
                self.graph[self.graph[vis_node].right].previousNode = vis_node

        path = []
        n = self.graph[self.goal_node_id].previousNode
        path.append(self.goal_node_id)
        while n != None:
            path.append(n)
            n = self.graph[n].previousNode
        path.reverse()
        self.path = None
        self.fullPath = visited
        return self.path, self.fullPath

    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        queue_ls = []
        full_path =[]
        self.graph[self.start_node_id].gOfN=0
        queue_ls.append(self.graph[self.start_node_id])
        while(queue_ls.__len__()!=0):
            currnt_node = min(queue_ls)
            full_path.append(currnt_node.id)
            queue_ls.remove(currnt_node)
            print(currnt_node.id, currnt_node.gOfN)
            if currnt_node == self.graph[self.goal_node_id]:
                break
            if currnt_node.up != -1 and self.graph[currnt_node.up].gOfN > currnt_node.gOfN +self.graph[
                currnt_node.up].edgeCost:
                self.graph[currnt_node.up].gOfN = currnt_node.gOfN +self.graph[currnt_node.up].edgeCost
                self.graph[currnt_node.up].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.up])
            if currnt_node.down != -1 and self.graph[currnt_node.down].gOfN > currnt_node.gOfN +self.graph[
                currnt_node.down].edgeCost:
                self.graph[currnt_node.down].gOfN = currnt_node.gOfN +self.graph[currnt_node.down].edgeCost
                self.graph[currnt_node.down].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.down])
            if currnt_node.left != -1 and self.graph[currnt_node.left].gOfN > currnt_node.gOfN + self.graph[
                currnt_node.left].edgeCost:
                self.graph[currnt_node.left].gOfN = currnt_node.gOfN + self.graph[currnt_node.left].edgeCost
                self.graph[currnt_node.left].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.left])
            if currnt_node.right != -1 and self.graph[currnt_node.right].gOfN > currnt_node.gOfN + self.graph[
                currnt_node.right].edgeCost:
                self.graph[currnt_node.right].gOfN = currnt_node.gOfN + self.graph[currnt_node.right].edgeCost
                self.graph[currnt_node.right].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.right])
        self.fullPath=full_path
        self.totalCost=self.graph[self.goal_node_id].gOfN
        path = []
        n = self.graph[self.goal_node_id].previousNode
        path.append(self.goal_node_id)
        while n != None:
            path.append(n)
            n = self.graph[n].previousNode
        path.reverse()
        self.path = None
        return self.path, self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        for key , val in self.graph.items():
            #print(self.xandy[key][0],self.xandy[key][1])
            self.graph[key].hOfN = math.sqrt(((self.xandy[key][0]-self.xandy[self.goal_node_id][0])**2)
                                               +((self.xandy[key][1]-self.xandy[self.goal_node_id][1])**2))
            #print(self.graph[key].hOfN , key)

        queue_ls = []
        full_path = []
        self.graph[self.start_node_id].gOfN = 0
        self.graph[self.start_node_id].heuristicFn = self.graph[self.start_node_id].hOfN
        queue_ls.append(self.graph[self.start_node_id])
        while (queue_ls.__len__() != 0):
            currnt_node = find_min_Heuristic(queue_ls)
            full_path.append(currnt_node.id)
            queue_ls.remove(currnt_node)
        #    print(currnt_node.heuristicFn)
            if currnt_node == self.graph[self.goal_node_id]:
                break
            if currnt_node.up != -1 and self.graph[currnt_node.up].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.up].hOfN:
                self.graph[currnt_node.up].gOfN = currnt_node.gOfN + self.graph[currnt_node.up].edgeCost
                self.graph[currnt_node.up].heuristicFn = self.graph[currnt_node.up].gOfN + self.graph[currnt_node.up].hOfN
                self.graph[currnt_node.up].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.up])
            if currnt_node.down != -1 and self.graph[currnt_node.down].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.down].hOfN:
                self.graph[currnt_node.down].gOfN = currnt_node.gOfN + self.graph[currnt_node.down].edgeCost
                self.graph[currnt_node.down].heuristicFn = self.graph[currnt_node.down].gOfN + self.graph[currnt_node.down].hOfN
                self.graph[currnt_node.down].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.down])
            if currnt_node.left != -1 and self.graph[currnt_node.left].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.left].hOfN:
                self.graph[currnt_node.left].gOfN = currnt_node.gOfN + self.graph[currnt_node.left].edgeCost
                self.graph[currnt_node.left].heuristicFn = self.graph[currnt_node.left].gOfN + self.graph[currnt_node.left].hOfN
                self.graph[currnt_node.left].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.left])
            if currnt_node.right != -1 and self.graph[currnt_node.right].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.right].hOfN:
                self.graph[currnt_node.right].gOfN = currnt_node.gOfN + self.graph[currnt_node.right].edgeCost
                self.graph[currnt_node.right].heuristicFn = self.graph[currnt_node.right].gOfN + self.graph[currnt_node.right].hOfN
                self.graph[currnt_node.right].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.right])
        self.fullPath = full_path
        self.totalCost = self.graph[self.goal_node_id].heuristicFn
        path = []
        n = self.graph[self.goal_node_id].previousNode
        path.append(self.goal_node_id)
        while n != None:
            path.append(n)
            n = self.graph[n].previousNode
        path.reverse()
        self.path = None
        return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        for key , val in self.graph.items():
            #print(self.xandy[key][0],self.xandy[key][1])
            self.graph[key].hOfN = abs(self.xandy[key][0]-self.xandy[self.goal_node_id][0]) + abs(self.xandy[key][1]-self.xandy[self.goal_node_id][1])
            #print(self.graph[key].hOfN , key)

        queue_ls = []
        full_path = []
        self.graph[self.start_node_id].gOfN = 0
        self.graph[self.start_node_id].heuristicFn = self.graph[self.start_node_id].hOfN
        queue_ls.append(self.graph[self.start_node_id])
        while (queue_ls.__len__() != 0):
            currnt_node = find_min_Heuristic(queue_ls)
            full_path.append(currnt_node.id)
            queue_ls.remove(currnt_node)
        #    print(currnt_node.heuristicFn)
            if currnt_node == self.graph[self.goal_node_id]:
                break
            if currnt_node.up != -1 and self.graph[currnt_node.up].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.up].hOfN and not(queue_ls.__contains__((self.graph[currnt_node.up]))):
                self.graph[currnt_node.up].gOfN = currnt_node.gOfN + self.graph[currnt_node.up].edgeCost
                self.graph[currnt_node.up].heuristicFn = self.graph[currnt_node.up].gOfN + self.graph[currnt_node.up].hOfN
                self.graph[currnt_node.up].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.up])
            if currnt_node.down != -1 and self.graph[currnt_node.down].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.down].hOfN and not(queue_ls.__contains__((self.graph[currnt_node.down]))):
                self.graph[currnt_node.down].gOfN = currnt_node.gOfN + self.graph[currnt_node.down].edgeCost
                self.graph[currnt_node.down].heuristicFn = self.graph[currnt_node.down].gOfN + self.graph[currnt_node.down].hOfN
                self.graph[currnt_node.down].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.down])
            if currnt_node.right != -1 and self.graph[currnt_node.right].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.right].hOfN:
                self.graph[currnt_node.right].gOfN = currnt_node.gOfN + self.graph[currnt_node.right].edgeCost
                self.graph[currnt_node.right].heuristicFn = self.graph[currnt_node.right].gOfN + self.graph[currnt_node.right].hOfN
                self.graph[currnt_node.right].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.right])
            if currnt_node.left != -1 and self.graph[currnt_node.left].heuristicFn > currnt_node.gOfN + self.graph[
                currnt_node.left].hOfN:
                self.graph[currnt_node.left].gOfN = currnt_node.gOfN + self.graph[currnt_node.left].edgeCost
                self.graph[currnt_node.left].heuristicFn = self.graph[currnt_node.left].gOfN + self.graph[currnt_node.left].hOfN
                self.graph[currnt_node.left].previousNode = currnt_node.id
                queue_ls.append(self.graph[currnt_node.left])
        self.fullPath = full_path
        self.totalCost = self.graph[self.goal_node_id].heuristicFn
        path = []
        n = self.graph[self.goal_node_id].previousNode

        while n != None:
            path.append(n)
            n = self.graph[n].previousNode
        path.reverse()
        self.path = None
        return self.path, self.fullPath, self.totalCost


def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
               #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

            #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [1, 1, 1, 1, 1, 1, 1, 1
                                                                                                             , 1, 1, 1, 1, 1, 1, 1
                                                                                                             , 1, 1, 1, 1, 1, 1, 1, 1
                                                                                                             , 1, 1, 1, 1, 1, 1, 1
                                                                                                             , 1, 1, 1, 1, 1])
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
'''s =SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])'''

