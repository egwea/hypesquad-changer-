import requests

#1. عشان خصوصيتك حط  التوكن حقك بنفسك 
TOKEN = "هنا_تحط_التوكن_حقك" 

# 2. الرابط الرسمي من ديسكورد المسؤول عن شارة الهايسبكواد
URL = "https://discord.com/api/v9/hypesquad/online"

# 3. إعدادات الطلب (الهيدرز) عشان ديسكورد يعرف إنك صاحب الحساب
headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

print("--- اختر العملية ---")
print("1 : انضمام/تغيير إلى بيت Bravery (البنفسجي)")
print("2 : انضمام/تغيير إلى بيت Brilliance (الأحمر)")
print("3 : انضمام/تغيير إلى بيت Balance (الأخضر)")
print("4 : حذف الشارة نهائياً")

choice = input("اختيارك: ")

# 4. تنفيذ العملية بناءً على اختيارك
if choice in ["1", "2", "3"]:
    # إذا تبي تضيف أو تغير، نرسل طلب POST ومعه رقم البيت
    payload = {"house_id": int(choice)}
    response = requests.post(URL, headers=headers, json=payload)
    
    if response.status_code == 204:
        print("✅ مبروك! تم تغيير الشارة بنجاح.")
    else:
        print(f"❌ فشل الطلب. كود الخطأ: {response.status_code}")

elif choice == "4":
    # إذا تبي تحذف الشارة، نرسل طلب DELETE لنفس الرابط بدون أي بيانات إضافية
    response = requests.delete(URL, headers=headers)
    
    if response.status_code == 204:
        print("🗑️ تم حذف الشارة من حسابك بنجاح.")
    else:
        print(f"❌ فشل الحذف. كود الخطأ: {response.status_code}")

else:
    print("❌ اختيار غير صحيح!")
