seat, room = map(float, input().split())

compartment = (seat - 1) // room + 1

print(compartment)
