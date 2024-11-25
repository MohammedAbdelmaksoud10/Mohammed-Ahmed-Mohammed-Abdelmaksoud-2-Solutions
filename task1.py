steps = []
StepDay = 0
for i in range(1,31):
    StepDay = int(input(f"Enter the number of steps you took on day {i}: "))
    steps.append(StepDay)
steps.sort(reverse=True)
print("="*30)
print(f"\"The most steps taken on a day is: {steps[0]}\"")
print(f"\"The least steps taken on a day is: {steps[-1]}\"")
sum = sum(steps)
print(f"\"The average number of steps taken per day is: {sum/len(steps)}\" step")
print(f"\"The list in descending order is: {steps}\"")
