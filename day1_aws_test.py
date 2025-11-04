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

