f = open("hallway.ply")


new_data = """,x,y,z,r,g,b
"""
index = 0
pt_num = 1
for line in f:
	index += 1
	if index % 1000 == 0:
		line = line.strip().split(" ")
		new_data += str(pt_num) + "," + str(float(line[0])*-100) + "," + str(float(line[1])*-100) + "," + str(float(line[2])*-100) + "," + str(int(line[-4])/255.0) + "," + str(int(line[-3])/255.0) + "," + str(int(line[-2])/255.0) + "\n"
		pt_num += 1


f.close()

f = open("test.csv", "w")
f.write(new_data)
f.close()