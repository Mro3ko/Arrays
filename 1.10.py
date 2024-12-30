test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

print(f"number of questions: {len(test_results)}")

correct_anwsers=0
for anwser in test_results:
    if anwser:
        correct_anwsers+=1

print(f"correct anwsers: {correct_anwsers}")

incorrect_anwsers=0
for anwser in test_results:
    if not anwser:
        incorrect_anwsers+=1

print(f"incorrect anwsers: {incorrect_anwsers}")
print(f"Percentage of correct answers: {round(correct_anwsers/len(test_results),2)*100}%")