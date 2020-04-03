# Stelios Zafeiris (A.M. 2015030076)

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = 3-cannibalLeft
		self.missionaryRight = 3-missionaryLeft
		self.parent = None
		self.visited = False

	def isGoal(self):
		return self.cannibalLeft == 0 and self.missionaryLeft == 0
	
	def isValid(self):
		return self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
               and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
               and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
               and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight)
			
	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft and \
			   self.boat == other.boat and self.cannibalRight == other.cannibalRight and \
			   self.missionaryRight == other.missionaryRight

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))
		
	def __str__(self):
		return f'({self.missionaryLeft}, {self.cannibalLeft}, {self.boat}, {self.missionaryRight}, {self.cannibalRight})'


def successors(examState):
	children = []
	if examState.boat == 1:
		newState = State(examState.cannibalLeft, examState.missionaryLeft - 2, 0)

		# (2, 0)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft - 2, examState.missionaryLeft, 0)

		# (0, 2)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft - 1, examState.missionaryLeft - 1, 0)

		# (1, 1)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft, examState.missionaryLeft - 1, 0)

		# (1, 0)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft - 1, examState.missionaryLeft, 0)

		# (0, 1)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
	else:
		newState = State(examState.cannibalLeft, examState.missionaryLeft + 2, 1)

		# (2, 0)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft + 2, examState.missionaryLeft, 1)

		# (0, 2)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft + 1, examState.missionaryLeft + 1, 1)

		# (1, 1)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft, examState.missionaryLeft + 1, 1)

		# (1, 0)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
		newState = State(examState.cannibalLeft + 1, examState.missionaryLeft, 1)

		# (0, 1)
		if newState.isValid():
			newState.parent = examState
			children.append(newState)
	return children

def BFS(initial_state):
	if initial_state.isGoal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.isGoal():
			return state
		state.visited = True
		children = successors(state)
		for child in children:
			if (not child.visited) or (child not in frontier):
				frontier.append(child)
	return None


if __name__ == "__main__":
    initial_state = State(3, 3, 1)
    result = BFS(initial_state)
    print("BFS algorithm result :")
    print ("(ML, CL, B, MR, CR)")
	
    path = []
    path.append(result)
    
	# Trace back the route to result node 
    parent = result.parent
    while parent:
        path.append(parent)
        parent = parent.parent
		
    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print(state)