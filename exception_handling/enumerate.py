# questions = [
#     "What is the capital of France?",
#     "Who wrote 'Hamlet'?",
#     "What is 2 + 2?"
# ]
#
# for i, question in enumerate(questions, start=3):
#     print(f"Q{i}: {question}")

# fruits = ['apple','banana','cherry']
# for x, fruit in enumerate(fruits,start=1):
#     print(f"{x}. {fruit}")

persons = [
    {'name': 'Zaw Ye Naung', 'rating': 9.9},
    {'name': 'Sat Paing Thu', 'rating': 9.5},
    {'name': 'Min Khant Ko', 'rating': 9.0}
]
for i, person in enumerate(persons, start=1):
    print(f"Customer {i}: {person['name']}, Rating = {person['rating']}")

