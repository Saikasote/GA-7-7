import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO, StringIO
import base64

# ==============================
# 1. Dataset provided
# ==============================
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Latin America,64.13,14,3.5
EMP002,IT,Middle East,68.47,8,4.3
EMP003,Marketing,Middle East,81.86,1,4.3
EMP004,R&D,Africa,93.72,6,4.8
EMP005,Operations,Europe,61.14,6,4.7
"""

# Convert to DataFrame
df = pd.read_csv(StringIO(data))

# ==============================
# 2. Frequency count for IT dept
# ==============================
it_count = df[df["department"] == "IT"].shape[0]

# ==============================
# 3. Create bar chart
# ==============================
plt.figure(figsize=(6,4))
df["department"].value_counts().plot(
    kind="bar", color="skyblue", edgecolor="black"
)
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

# Save plot to base64 string
buf = BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode("utf-8")
buf.close()

# ==============================
# 4. Generate HTML file
# ==============================
html_content = f"""
<html>
<head><title>Employee Performance Analysis</title></head>
<body>
<h2>Employee Distribution by Department</h2>
<p><strong>Email:</strong> 23f1002151@ds.study.iitm.ac.in</p>
<p>Frequency count for IT department: {it_count}</p>
<img src="data:image/png;base64,{img_base64}" />
</body>
</html>
"""

# ==============================
# 5. Save to file
# ==============================
with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file generated: employee_analysis.html")
