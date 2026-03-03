import sqlite3
import os
from pathlib import Path

# Prüfen, ob wir auf Render laufen
if os.getenv("RENDER"):
    DB_PATH = Path("/data/faq.db")
else:
    BASE_DIR = Path(__file__).resolve().parent
    DB_PATH = BASE_DIR / "data" / "faq.db"


def init_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create FAQ table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intent TEXT NOT NULL UNIQUE,
            answer TEXT NOT NULL
        );
    """)

    # Sample data 
    sample_data = [
        ("Are there specific certifications required before onboarding?", "Suppliers are required to hold relevant compliance certifications prior to onboarding. The specific certifications depend on the nature of the goods or services provided and may include industry standards, regulatory approvals, or quality management certifications. All required documentation must be submitted during the onboarding process and is subject to review and verification. Additional certifications may be requested as regulations or business requirements change."),
        ("How are product defects or disputes handled?", "If a product defect or issue arises, we ask suppliers to notify us promptly with full details and supporting documentation (e.g., photos, batch numbers, delivery references). Our quality team will review the case and work collaboratively to determine the root cause and agree on corrective actions. Depending on the situation, this may include replacement, repair, credit, or other mutually agreed resolutions. Our goal is to resolve issues quickly, fairly, and in a way that maintains a strong, long-term partnership."),
        ("What sustainability standards must suppliers meet?", "Suppliers must comply with applicable ESG regulations and the voestalpine Supplier Code of Conduct, covering environmental protection, human rights, labor standards, health and safety, and ethical business practices. Evidence of compliance and continuous improvement may be required."),
        ("What are the payment terms and conditions for suppliers?","Our standard payment terms are 30 days from the date of invoice, unless otherwise agreed upon in the contract. Payments are processed via bank transfer to the account details provided on the invoice. Late payments are subject to a 2% late fee for every 30 days beyond the due date. For first-time suppliers or larger contracts, we may require advance payment or a deposit. Payment terms for special projects or high-value orders will be agreed upon individually, depending on the specifics of the contract.")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO faq (intent, answer)
        VALUES (?, ?);
    """, sample_data)

    conn.commit()
    conn.close()

    print(f"Database successfully initialized at: {DB_PATH}")


if __name__ == "__main__":
    init_database()