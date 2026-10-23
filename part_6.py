for i in range(5):
    print(i)

scores=[70,50,60,80,65]
for score in scores:
    print(score)

count = 1
while count <=5:
    print(count)
    count +=1

scores = [70,35,20,90,45]

total = 0
passing_score=0
failing_score=0
for score in scores:
    total += score
    
average = total /len(scores)

print("Total:",total)
print("Average:",average)

for score in scores:
    if score <40:
       failing_score +=1
    else:
       passing_score +=1

print(f"No Pass: {passing_score}")
print(f"No fail: {failing_score}")