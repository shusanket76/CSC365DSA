f = open("demofile2.txt", "a")
f.write("  2                         Now the file has more content!")
f.write("\n")
f.write("3kdskc")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())