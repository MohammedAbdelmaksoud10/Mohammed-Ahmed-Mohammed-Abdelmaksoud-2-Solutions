books = [
    ["Atomic Hapits", 10], ["Rich Dad Poor Dad", 7], ["The Power of Habit", 5],
    ["Club of the Coders", 6], ["Think and Grow Rich", 8], ["The Alchemist", 9], ["The Secret", 5]]

bookStore = dict(books)

totalDays = sum(bookStore.values())
averageBorrowd = totalDays / len(bookStore)
max_borrowd = max(bookStore.values())
min_borrowd = min(bookStore.values())
    
sorted_books = sorted(bookStore.items(), key=lambda x: x[1], reverse=True)

print("The books in descending order: ")
for title, days in sorted_books:
    print(f"{title} - {days} days")
print("="*50)
print(f"\"Total number of days: {totalDays}\"")
print(f"\"Average number of days borrowed: {averageBorrowd:.2f}\"")
print(f"\"The largest number of days borrowed: {max_borrowd}\" days")
print(f"\"The smallest number of days borrowed: {min_borrowd} days\"")