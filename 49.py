import os, time

highscore = 0
name = None

f =open ("highscores.txt", "r")
scores = f.read().split("\n")
f.close()

for rows in scores:
    data = rows.split()
    if data != []:
        if int(data[1]) > highscore:
            highscore = int(data[1])
            name = data[0]

print("The highscore is", highscore, "by", name)
            