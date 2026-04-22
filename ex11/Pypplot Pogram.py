import matplotlib.pyplot as plt
department=['CSE','ECE','EEE','MECH','CIVIL']
faculty_count=[25,18,15,20,10]
plt.figure(figsize=(8,5))
plt.bar(department,faculty_count,color='skyblue',edgecolor='black')
plt.xlabel("Department")
plt.ylabel("Faculty Count")
plt.title("Faculty count bu Department")
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show()
