
input()  
scores = list(map(int, input().split()))
unique_scores = set(scores)
if len(unique_scores) < 2:
    print("Not enough unique scores to determine the runner-up.")
else:
    sorted_unique_scores = sorted(unique_scores)
    runner_up_score = sorted_unique_scores[-2]
    print(runner_up_score)
