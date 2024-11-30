from z3 import *

hails = []
i = 0
for line in open("input.txt"):
    if(i > 2):
        break
    position, velocity = line.strip().split("@")
    position = tuple(map(int, position.split(",")))
    velocity = tuple(map(int, velocity.split(",")))
    hails.append((position, velocity))
    i += 1

for idx, hail in enumerate(hails):
    for axis, axis_idx in [("x", 0), ("y", 1), ("z", 2)]:
        print(f"v{axis} * t{idx} + i{axis} == {hails[idx][1][axis_idx]} * t{idx} + {hails[idx][0][axis_idx]},")

vx = Int("vx")
vy = Int("vy")
vz = Int("vz")
ix = Int("ix")
iy = Int("iy")
iz = Int("iz")
t0 = Int("t0")
t1 = Int("t1")
t2 = Int("t2")

solve(
    # Replace with output from previous part
)

# Replace with output values from solver
print(ix + iy + iz) 