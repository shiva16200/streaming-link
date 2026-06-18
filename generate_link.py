#!/usr/bin/env python3
import base64
import hashlib
import time
from datetime import datetime

# ==========================================
# तपाईंको आफ्नै जानकारी यहाँ भर्नुहोस्
# ==========================================
SERVER_IP = "202.166.192.207"  # तपाईंको server को IP
STREAM_NAME = "wc-Himalaya3"  # Stream को नाम
SECRET_KEY = "mytopsecret123"  # तपाईंले रोजेको पासवर्ड
# ==========================================

def generate_link():
    """लिङ्क बनाउने फंक्शन"""
    
    # हालको समय लिनुहोस्
    current_time = int(time.time())
    
    # 24 घण्टाको लागि मान्य (1440 मिनेट)
    valid_minutes = 1440
    
    # सुरक्षाको लागि स्ट्रिङ बनाउनुहोस्
    auth_string = f"server_time={current_time}&valid_minutes={valid_minutes}&id=200"
    
    # MD5 हैश बनाउनुहोस्
    hash_value = hashlib.md5(f"{auth_string}{SECRET_KEY}".encode()).hexdigest()
    
    # Base64 मा कन्भर्ट गर्नुहोस्
    wms_auth = base64.b64encode(
        f"{auth_string}&hash_value={hash_value}".encode()
    ).decode()
    
    # पूरो लिङ्क बनाउनुहोस्
    link = f"http://{SERVER_IP}/ffplay/{STREAM_NAME}/playlist.m3u8?wmsAuthSign={wms_auth}"
    
    return link

# ==========================================
# मुख्य कार्यक्रम
# ==========================================
if __name__ == "__main__":
    # लिङ्क बनाउनुहोस्
    link = generate_link()
    
    # README फाइल बनाउनुहोस्
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    readme_content = f"""# 📺 मेरो स्ट्रिमिङ लिङ्क

    
## ⏰ उत्पादन मिति
{current_time}

## ✅ स्थिति
- **सक्रिय**: हो
- **म्याद**: २४ घण्टा

## 🔄 स्वचालित ताजा
यो लिङ्क हरेक २४ घण्टामा स्वचालित रूपमा ताजा हुन्छ।

## 📥 प्रयोग गर्ने तरिका
- VLC मा: File → Open Network → लिङ्क पेस्ट गर्नुहोस्
- ब्राउजरमा: HLS प्लेयर मार्फत हेर्नुहोस्
"""
    
    # README.md मा लेख्नुहोस्
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # सन्देश देखाउनुहोस्
    print("✅ लिङ्क सफलतापूर्वक बनाइयो!")
    print(f"📍 {link}")

## 🌐 हालको लिङ्क
