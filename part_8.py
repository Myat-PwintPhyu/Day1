scores = [55,80,35,90,65]

scores.append(75)
print(scores)
scores[1] = 85
print(scores)

print(f"highest = {max(scores)}")
print(f"lowest = {min(scores)}")

print (f"average = {sum(scores)/len(scores)}")

for score in scores:
    if (score >= 80):
        print(score)