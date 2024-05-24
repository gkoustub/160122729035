from collections import defaultdict

jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):
    # Check if we have reached the goal
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    
    # If we haven't visited this state before
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        
        # Try all possible actions
        return (waterJugSolver(0, amt2) or  # Empty Jug1
                waterJugSolver(amt1, 0) or  # Empty Jug2
                waterJugSolver(jug1, amt2) or  # Fill Jug1
                waterJugSolver(amt1, jug2) or  # Fill Jug2
                waterJugSolver(amt1 + min(amt2, (jug1 - amt1)), amt2 - min(amt2, (jug1 - amt1))) or  # Pour Jug2 -> Jug1
                waterJugSolver(amt1 - min(amt1, (jug2 - amt2)), amt2 + min(amt1, (jug2 - amt2))))   # Pour Jug1 -> Jug2
    else:
        return False

print("Steps:")
if not waterJugSolver(0, 0):
    print("No solution found.")
