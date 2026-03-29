# Your first Python script - Phase 1 Week 1
name = "Saurav"
skills = ["Python", "FastAPI", "PostgreSQL", "ML"]

print(f"Engineer: {name}")
print(f"Building toward: {skills[-1]}")
print()

for i, skill in enumerate(skills, 1):
    print(f"  Step {i}: {skill}")

print()
print("Status: Under construction. Deliberately.")