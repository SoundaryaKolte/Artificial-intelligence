# Take input
n = int(input("Enter number of jobs: "))
jobs = []

print("Enter each job as: ID Deadline Profit")
for _ in range(n):
    job_id, deadline, profit = input().split()
    deadline = int(deadline)
    profit = int(profit)
    jobs.append((job_id, deadline, profit))

# Sort jobs by profit (highest first)
jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)
slots = [None] * max_deadline
total_profit = 0

for job in jobs:
    job_id, deadline, profit = job
    for i in range(deadline - 1, -1, -1):
        if slots[i] is None:
            slots[i] = job_id
            total_profit += profit
            break

# Output
scheduled_jobs = [job for job in slots if job is not None]
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)
