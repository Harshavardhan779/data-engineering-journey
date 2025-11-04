"""
Day 1: AWS S3 Connection Test
Created: November 4, 2025
Purpose: Test AWS credentials and S3 access
"""

import boto3
from datetime import datetime

def test_s3_connection():
    """Test connection to AWS S3"""
    try:
        # Initialize S3 client
        s3 = boto3.client('s3')
        
        # List all buckets
        response = s3.list_buckets()
        
        print("✅ AWS S3 Connection Successful!")
        print(f"\n📦 Your S3 Buckets:")
        
        for bucket in response['Buckets']:
            print(f"  - {bucket['Name']} (Created: {bucket['CreationDate']})")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Make sure AWS credentials are configured")

if __name__ == "__main__":
    print("=" * 50)
    print("AWS S3 CONNECTION TEST")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    print()
    
    test_s3_connection()

# Next steps:
# 1. Install boto3: pip install boto3
# 2. Configure AWS credentials
# 3. Run this script to verify connection
```

4. **Commit message:** "Add Day 1 AWS S3 test script"

5. **Click:** "Commit changes"

**🎉 Your GitHub portfolio is LIVE!**

---

## **💼 PHASE 3: LINKEDIN UPDATE (25 mins)**

### **Step 1: Login to LinkedIn**
**Link:** https://www.linkedin.com/

---

### **Step 2: Update Headline (5 mins)**

1. **Click:** Your profile picture (top right)
2. **Click:** "View Profile"
3. **Click:** Pencil icon next to your name
4. **Headline field, replace with:**
```
Aspiring Data Engineer | Oracle PL/SQL Production Experience | Python | AWS | Building Cloud Data Pipelines | AIML @ Saveetha Engineering College
```

5. **Save**

---

### **Step 3: Update About Section (10 mins)**

1. **Click:** Pencil icon on "About" section
2. **Replace with:**
```
🚀 Data Engineering Enthusiast | Building the Future of Data Infrastructure

Currently transitioning from Oracle development to modern cloud-based data engineering. Combining traditional database expertise with cutting-edge cloud technologies.

💼 CURRENT ROLE
Software Engineer Intern @ Azentio
- Working with Oracle PL/SQL, Forms, and Reports
- Managing production change requests
- Resolving system stability issues
- Collaborating with cross-functional teams

🎓 EDUCATION
B.Tech in Artificial Intelligence & Machine Learning
Saveetha Engineering College, Chennai (2022-2026)

🛠️ TECHNICAL SKILLS
Languages: Python, SQL, PL/SQL, Java
Cloud: AWS (S3, RDS, Lambda, Glue)
Databases: Oracle, MySQL, PostgreSQL
ETL: Apache Airflow (learning)
Libraries: Pandas, NumPy, Scikit-Learn, Flask
Tools: Git, Jupyter, VS Code

📊 WHAT I'M BUILDING
- Oracle-to-Cloud migration pipelines
- End-to-end ETL workflows
- Data analytics solutions
- ML model deployment infrastructure

🎯 2025 GOAL
Secure a Data Engineer role where I can leverage my Oracle expertise while building modern cloud data pipelines.

📚 CURRENTLY LEARNING
- Apache Airflow for workflow orchestration
- AWS data services (Glue, Redshift, Kinesis)
- Advanced SQL optimization
- Real-time data streaming

💡 MY UNIQUE VALUE
Most data engineers don't understand legacy databases. Most database engineers don't understand modern data pipelines. I'm building expertise in both.

🤝 LET'S CONNECT
Always open to connecting with fellow data engineers, mentors, and anyone passionate about data infrastructure. Feel free to reach out!

📫 harshavardhanbv779@gmail.com
🔗 GitHub: github.com/[your-username]/data-engineering-journey

---
"Turning data chaos into structured insights, one pipeline at a time."
```

3. **Save**

---

### **Step 4: Add/Update Skills (5 mins)**

**Click:** "Add profile section" → "Add skills"

**Add these skills (in order of priority):**
1. Data Engineering
2. Apache Airflow
3. ETL (Extract, Transform, Load)
4. AWS (Amazon Web Services)
5. Python
6. SQL
7. PL/SQL
8. Oracle Database
9. Data Pipelines
10. Cloud Computing
11. Data Warehousing
12. PostgreSQL
13. MySQL
14. Git
15. Machine Learning

---

### **Step 5: Follow Data Engineering Leaders (5 mins)**

**Search and follow these people:**

1. **Zach Wilson** - Seattle Data Guy
   https://www.linkedin.com/in/eczachly/

2. **Andreas Kretz** - LearnDataEngineering
   https://www.linkedin.com/in/andreas-kretz/

3. **Joseph Machado** - Start Data Engineering
   https://www.linkedin.com/in/josephmachado1991/

4. **Sumit Mittal** - Data Engineering Simplified
   https://www.linkedin.com/in/bigdatabysumit/

5. **Ben Rogojan** - Seattle Data Guy
   https://www.linkedin.com/in/benjaminrogojan/

**Turn on notifications** for their posts!

---

## **📝 PHASE 4: REFLECTION & PLANNING (30 mins)**

### **Step 1: Create Day 1 Journal (15 mins)**

**On your computer, create:** `Data_Engineering_Journal.txt`

**Write this:**
```
========================================
DATA ENGINEERING JOURNEY - JOURNAL
========================================

DAY 1 - NOVEMBER 4, 2025
Time: [Your current time]
Total time invested today: ~3 hours

WHAT I ACCOMPLISHED:
✅ Created AWS Free Tier account
✅ Set up billing protection ($1 threshold)
✅ Created S3 bucket and uploaded data
✅ Watched 3 Data Engineering videos
✅ Created GitHub repository with detailed README
✅ Updated LinkedIn profile completely
✅ Followed 5 data engineering leaders

NEW CONCEPTS I LEARNED:
1. Data Engineering vs Data Science - clear differences
2. ETL (Extract, Transform, Load) pipelines
3. Apache Airflow for workflow orchestration
4. AWS S3 for cloud storage at scale
5. DAGs (Directed Acyclic Graphs) in Airflow
6. [Add 5 more from your video notes]

TOOLS I'M NOW AWARE OF:
- Apache Airflow (workflow orchestration)
- AWS Glue (ETL service)
- Apache Spark (big data processing)
- dbt (data build tool)
- [Add more from videos]

WHAT CONFUSED ME:
1. [Write down anything that wasn't clear]
2. [Questions you have]
3. [Concepts to revisit]

HOW I FEEL:
[Write 3-5 sentences about your emotions, energy, confidence]

CHALLENGES FACED TODAY:
1. AWS billing setup was initially confusing
2. [Add others]

HOW I OVERCAME THEM:
1. Followed step-by-step instructions carefully
2. [Add others]

KEY INSIGHTS:
1. Data Engineering is more about infrastructure than algorithms
2. My Oracle experience is actually valuable and rare
3. Cloud skills are essential for modern data engineering
4. [Add your own insights]

TOMORROW'S COMMITMENT:
I will spend at least 1 hour on:
[List specific tasks for Day 2]
```

---

### **Step 2: Plan Day 2 Specifically (10 mins)**

**Create:** `Day2_Plan.txt`
```
DAY 2 PLAN - NOVEMBER 5, 2025
Target time: 1-2 hours

MORNING (Optional - 15 mins):
□ Read Day 1 journal
□ Review GitHub repository
□ Check AWS billing (should still be $0)

EVENING SESSION (60-90 mins):
□ Watch "SQL for Data Engineering" video (20 mins)
□ Practice 5 SQL problems on LeetCode (25 mins)
□ Create Python script to connect to AWS S3 (15 mins)
□ Update GitHub with Day 2 progress (10 mins)

RESOURCES NEEDED:
- LeetCode account (free)
- Python boto3 library
- AWS credentials

SUCCESS CRITERIA:
✓ Complete at least 3/4 tasks
✓ Update GitHub
✓ Feel confident about progress
