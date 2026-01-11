names = ["Snigdh","Rishima","Ishita","Harshul","Akshat","Drishtant","Avni"]
bills = [90, 75, 100, 65, 80, 120, 50]

for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")