# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  visited = set()
  frontier = util.Stack() # last in, first out

  frontier.push((problem.getStartState(),[],0))

  while frontier:
    
    state,actions,cost = frontier.pop()
    
    if state in visited:
      continue
    
    visited.add(state)

    if problem.isGoalState(state) == True:
      break

    for nextState, action, cost in problem.getSuccessors(state):
      if nextState not in visited:
        frontier.push((nextState,actions + [action],cost))
        
  return actions

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  visited = set()
  frontier = util.Queue() # first in, first out

  frontier.push((problem.getStartState(),[],0))

  while frontier:
    
    state,actions,cost = frontier.pop()
    
    if state in visited:
      continue
    
    visited.add(state)

    if problem.isGoalState(state) == True:
      break

    for nextState, action, cost in problem.getSuccessors(state):
      if nextState not in visited:
        frontier.push((nextState,actions + [action],cost))
        
  return actions
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  
  visited = set()
  frontier = util.PriorityQueue()
  
  frontier.push((problem.getStartState(),[],0),0)
  
  while frontier:
    state,actions,costs = frontier.pop()
    
    if state in visited:
      continue
    
    visited.add(state)

    if problem.isGoalState(state) == True:
      break

    for nextState, action, cost in problem.getSuccessors(state):
      if nextState not in visited:
        frontier.push((nextState,actions + [action],costs + cost),costs+cost)

  return actions

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  
  visited = set()
  frontier = util.PriorityQueue()

  state = problem.getStartState()
  h = heuristic(state, problem)
  frontier.push((state,[],0),h)

  while frontier:
    state,actions,costs = frontier.pop()
    
    if state in visited:
      continue

    visited.add(state)
    
    if problem.isGoalState(state) == True:
      break

    for nextState, action, cost in problem.getSuccessors(state):
      if nextState not in visited:
        h = heuristic(nextState, problem)
        frontier.push((nextState,actions + [action],costs + cost),costs+cost+h)

  return actions
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
