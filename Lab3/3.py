def sum(heads,legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if (chickens * 2 + rabbits * 4) == legs:
            return chickens, rabbits

heads = int(input())
legs = int(input())
chickens,rabbits = sum(heads,legs)
print(f"chickens: {chickens},rabbits: {rabbits}")