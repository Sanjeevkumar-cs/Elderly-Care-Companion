# test_db_integration.py
from database import (
    create_tables, 
    add_sample_data,
    get_all_medications,
    get_refill_alerts,
    get_daily_summary,
    save_conversation,
    get_upcoming_appointments
)

print("="*50)
print("Testing Database Integration")
print("="*50)

# Initialize database
print("\n1️⃣ Creating tables...")
create_tables()

print("\n2️⃣ Adding sample data...")
add_sample_data()

# Test medication display
print("\n3️⃣ Fetching medications...")
meds = get_all_medications(1)
for med in meds:
    print(f"   💊 {med['name']}: {med['pill_count']} pills left")

# Test refill alerts
print("\n4️⃣ Checking refill alerts...")
print(f"   {get_refill_alerts(1)}")

# Test daily summary
print("\n5️⃣ Daily Summary:")
print(get_daily_summary(1))

# Test saving conversation
print("\n6️⃣ Testing save conversation...")
save_conversation(1, "I have a headache", "Take rest and drink water", False)

print("\n✅ All tests passed! Database is ready for Gradio app.")