power_strength = [[12.0, 1], [11.0, 1.0], [10.0, 3.0], [9.0, 5.0], [8.0, 7.0], [7.0, 9.0], [6.0, 11.0]]
endurance_isometric = [[3.0, 64.0], [5.0, 54.0], [7.0, 45.0], [9.0, 36.0], [11.0, 24.0], [12.0, 21.0]]


power_strength = [[int(i[0]), int(i[1])] for i in endurance_isometric]

print(power_strength)