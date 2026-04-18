import sqlite3

DB_NAME = "college_chatbot.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT UNIQUE,
            answer TEXT,
            category TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_default_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Prevent duplicate insertion
    cursor.execute("SELECT COUNT(*) FROM faqs")
    count = cursor.fetchone()[0]

    if count > 0:
        conn.close()
        return

    sample_data = [
        # Admissions (1-15)
        ("What is the admission process?", "You can apply online through the college admission portal and submit required documents.", "Admissions"),
        ("What documents are required for admission?", "Students usually need 10th and 12th mark sheets, ID proof, passport-size photographs, transfer certificate, and migration certificate if applicable.", "Admissions"),
        ("Can I take direct admission in GEHU?", "Admission depends on eligibility criteria and university rules. You should contact the admission office for updated details.", "Admissions"),
        ("Is there an entrance exam for admission?", "Some courses may require entrance exams or merit-based selection depending on university guidelines.", "Admissions"),
        ("How can I apply for admission online?", "You can visit the official university website, fill out the online application form, upload documents, and pay the registration fee.", "Admissions"),
        ("What is the eligibility for BCA?", "Students who have passed 12th class from a recognized board are generally eligible for BCA admission.", "Admissions"),
        ("What is the eligibility for BBA?", "Students who have passed 12th class from a recognized board are generally eligible for BBA admission.", "Admissions"),
        ("What is the eligibility for MBA?", "A valid bachelor’s degree may be required for MBA admission.", "Admissions"),
        ("Can diploma students apply for admission?", "Yes, diploma students may apply for selected courses depending on university policy.", "Admissions"),
        ("When does the admission process start?", "Admissions usually begin after board or university results are declared.", "Admissions"),
        ("Can I apply offline for admission?", "Most admissions are online, but students can visit campus for guidance.", "Admissions"),
        ("Is counseling available for admission?", "Yes, admission counseling and support are available for students.", "Admissions"),
        ("Can international students apply?", "Yes, international admissions may be available as per university rules.", "Admissions"),
        ("Is admission based on merit?", "Many programs offer admission based on merit and eligibility.", "Admissions"),
        ("Can I change my course after admission?", "Course change may be possible only under university rules and seat availability.", "Admissions"),

        # Fees (16-25)
        ("What are the fees for BCA?", "The BCA course fee is approximately ₹45,000 per semester.", "Fees"),
        ("What are the fees for BBA?", "The BBA fee structure may vary each year. Please verify with the fee department.", "Fees"),
        ("What are the fees for MBA?", "MBA fees depend on specialization and academic session.", "Fees"),
        ("Can fees be paid in installments?", "In some cases, installment options may be available as per university policies.", "Fees"),
        ("Is there any registration fee?", "Yes, an admission or registration fee may be required during the admission process.", "Fees"),
        ("Are hostel fees separate from course fees?", "Yes, hostel and mess charges are separate from academic fees.", "Fees"),
        ("Can fees be paid online?", "Yes, fees can usually be paid through online payment modes.", "Fees"),
        ("Is there any late fee penalty?", "Yes, late fee charges may apply if payment is delayed.", "Fees"),
        ("Are examination fees included?", "Exam fees may be separate depending on university rules.", "Fees"),
        ("Can I get a fee receipt?", "Yes, students receive fee payment receipts after successful payment.", "Fees"),

        # Courses (26-40)
        ("What courses are offered?", "We offer BCA, BBA, B.Com, MCA, MBA, and other UG/PG programs.", "Courses"),
        ("Does GEHU offer MCA?", "Yes, GEHU offers MCA as a postgraduate computer applications program.", "Courses"),
        ("Does GEHU offer B.Tech?", "Yes, GEHU offers B.Tech in different engineering branches.", "Courses"),
        ("Are postgraduate courses available?", "Yes, postgraduate courses like MCA, MBA, M.Com, and M.Sc are available.", "Courses"),
        ("Does GEHU offer management courses?", "Yes, management-related courses such as BBA and MBA are available.", "Courses"),
        ("Is BCA with AI & Data Science available?", "Yes, such specialization-based programs may be available depending on the academic session.", "Courses"),
        ("Is BCA available?", "Yes, BCA is available as an undergraduate computer applications course.", "Courses"),
        ("Is BBA available?", "Yes, BBA is available as an undergraduate management course.", "Courses"),
        ("Is MBA available?", "Yes, MBA is available for postgraduate students.", "Courses"),
        ("Is law available?", "Yes, law-related programs may be available depending on campus offerings.", "Courses"),
        ("Is pharmacy available?", "Yes, pharmacy programs may be offered depending on university departments.", "Courses"),
        ("Are diploma courses available?", "Some diploma or certificate-based programs may be available.", "Courses"),
        ("Does GEHU offer commerce courses?", "Yes, commerce-related programs like B.Com may be available.", "Courses"),
        ("Are computer science courses available?", "Yes, computer-related programs like BCA, MCA, and B.Tech are available.", "Courses"),
        ("Are skill-based courses available?", "Yes, students may get access to skill development and certification programs.", "Courses"),

        # Hostel (41-50)
        ("Is hostel available?", "Yes, hostel facilities are available for boys and girls.", "Hostel"),
        ("What are the hostel facilities?", "The college provides separate hostel facilities for boys and girls with Wi-Fi and mess.", "Hostel"),
        ("Is hostel available for girls?", "Yes, separate hostel accommodation is available for girls.", "Hostel"),
        ("Is hostel available for boys?", "Yes, separate hostel accommodation is available for boys.", "Hostel"),
        ("Does hostel have Wi-Fi?", "Yes, hostel facilities may include Wi-Fi depending on hostel rules and availability.", "Hostel"),
        ("Is mess facility available in hostel?", "Yes, hostel students are usually provided mess facilities.", "Hostel"),
        ("Are hostel rooms shared?", "Yes, hostel rooms may be single, double, or triple sharing depending on availability.", "Hostel"),
        ("Is laundry available in hostel?", "Laundry facilities may be available depending on hostel services.", "Hostel"),
        ("Can day scholars apply for hostel later?", "Yes, depending on room availability and hostel rules.", "Hostel"),
        ("Are hostel rules strict?", "Yes, students are expected to follow hostel discipline and timing rules.", "Hostel"),

        # Exams (51-60)
        ("What is the exam schedule?", "The exam schedule is usually announced on the college notice board and official website.", "Exams"),
        ("Where can I check exam dates?", "Exam dates are usually displayed on the notice board, student portal, or official university website.", "Exams"),
        ("How are internal exams conducted?", "Internal exams are generally conducted by departments during the semester.", "Exams"),
        ("Where can I get my admit card?", "Admit cards are usually provided through the student portal or department.", "Exams"),
        ("How can I check my result?", "Results are usually published through the university portal or official announcements.", "Exams"),
        ("Are practical exams conducted?", "Yes, practical exams are conducted for lab-based and technical subjects.", "Exams"),
        ("Can I apply for rechecking?", "Yes, students may apply for rechecking or revaluation as per university rules.", "Exams"),
        ("What happens if I miss an exam?", "Students should contact the examination department for guidance in such cases.", "Exams"),
        ("How many internal exams are there?", "The number of internal exams may depend on the course and semester.", "Exams"),
        ("Is attendance required for exams?", "Yes, minimum attendance may be required to appear in examinations.", "Exams"),

        # Campus (61-75)
        ("Where is the library?", "The library is located in Block A, 2nd floor.", "Campus"),
        ("What are the college timings?", "The college timings are generally from 9:00 AM to 4:00 PM.", "Campus"),
        ("Where is the canteen?", "The canteen is located near the main academic block.", "Campus"),
        ("Are there computer labs in college?", "Yes, GEHU has computer labs for practical and technical learning.", "Campus"),
        ("Is WiFi available?", "Yes, WiFi is available on campus.", "Campus"),
        ("Is Wi-Fi available on campus?", "Yes, Wi-Fi access may be available in academic and campus areas.", "Campus"),
        ("Does the campus have sports facilities?", "Yes, students can participate in sports and physical activities on campus.", "Campus"),
        ("Is there a medical room on campus?", "Basic medical support may be available on campus.", "Campus"),
        ("Are smart classrooms available?", "Yes, many classrooms may be equipped with digital teaching facilities.", "Campus"),
        ("Is there a seminar hall?", "Yes, seminar halls are available for events and academic sessions.", "Campus"),
        ("Does campus have CCTV security?", "Yes, campus areas may be monitored for safety and security.", "Campus"),
        ("Is parking available for students?", "Parking may be available depending on campus policy.", "Campus"),
        ("Is there a gym on campus?", "Gym or fitness facilities may be available for students.", "Campus"),
        ("Are cultural events organized?", "Yes, cultural programs and annual events are organized regularly.", "Campus"),
        ("Is there an auditorium in college?", "Yes, auditoriums or event halls may be available for functions and seminars.", "Campus"),

        # Transport (76-82)
        ("Is transport available?", "Yes, transport facilities are available on selected routes.", "Transport"),
        ("Is bus facility available for students?", "Yes, transport facilities are available on selected routes.", "Transport"),
        ("How can I know my bus route?", "Bus route details can be obtained from the transport department or administration office.", "Transport"),
        ("Is transport fee separate?", "Yes, transport charges are generally separate from tuition fees.", "Transport"),
        ("Can I apply for transport later?", "Yes, transport facility may be applied for later depending on seat availability.", "Transport"),
        ("Are buses available for all areas?", "Transport coverage depends on route availability and demand.", "Transport"),
        ("Is bus timing fixed?", "Yes, buses usually operate on fixed pickup and drop timings.", "Transport"),

        # Scholarship (83-90)
        ("Is scholarship available?", "Yes, scholarships are available based on merit.", "Scholarship"),
        ("Who can apply for scholarship?", "Scholarship eligibility depends on academic merit, category, and university policy.", "Scholarship"),
        ("Is merit scholarship available?", "Yes, merit-based scholarships may be available for eligible students.", "Scholarship"),
        ("How can I apply for scholarship?", "Students can apply through the scholarship process defined by the university.", "Scholarship"),
        ("Can scholarship continue every year?", "Scholarship continuation may depend on academic performance and rules.", "Scholarship"),
        ("Is there scholarship for toppers?", "Yes, top-performing students may be eligible for merit scholarship.", "Scholarship"),
        ("Does GEHU provide financial support?", "Some scholarship and financial support options may be available.", "Scholarship"),
        ("Can reserved category students get scholarship?", "Scholarship support may be available as per government or university schemes.", "Scholarship"),

        # Placements (91-100)
        ("Are placements available?", "Yes, the university provides placement support and career guidance.", "Placements"),
        ("Does GEHU provide placements?", "Yes, the university provides placement assistance and career support.", "Placements"),
        ("Are companies invited for campus placement?", "Yes, companies may visit campus for recruitment drives.", "Placements"),
        ("Is placement training available?", "Yes, placement preparation and skill development sessions are conducted.", "Placements"),
        ("Do students get internship support?", "Yes, internship opportunities and guidance are provided.", "Placements"),
        ("Which students can sit in placements?", "Placement eligibility usually depends on academic performance and company criteria.", "Placements"),
        ("Are mock interviews conducted?", "Yes, mock interviews and aptitude preparation may be provided.", "Placements"),
        ("Is resume building support available?", "Yes, students may get support for resume preparation.", "Placements"),
        ("Are soft skills classes conducted?", "Yes, communication and soft skills sessions are often conducted.", "Placements"),
        ("Do final year students get placement support?", "Yes, final year students generally receive placement assistance.", "Placements")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO faqs (question, answer, category)
        VALUES (?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()


def get_all_faqs(limit=None):
    conn = get_connection()
    cursor = conn.cursor()

    if limit:
        cursor.execute("SELECT * FROM faqs ORDER BY id DESC LIMIT ?", (limit,))
    else:
        cursor.execute("SELECT * FROM faqs ORDER BY id DESC")

    data = cursor.fetchall()
    conn.close()
    return data


def get_total_faqs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM faqs")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def add_faq(question, answer, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO faqs (question, answer, category) VALUES (?, ?, ?)",
        (question, answer, category)
    )
    conn.commit()
    conn.close()


def delete_faq(faq_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM faqs WHERE id = ?", (faq_id,))
    conn.commit()
    conn.close()


def get_faq_by_id(faq_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM faqs WHERE id = ?", (faq_id,))
    data = cursor.fetchone()
    conn.close()
    return data


def update_faq(faq_id, question, answer, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE faqs SET question=?, answer=?, category=? WHERE id=?
    """, (question, answer, category, faq_id))
    conn.commit()
    conn.close()


def search_faqs(search="", category="", limit=20):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM faqs WHERE 1=1"
    params = []

    if search:
        query += " AND (question LIKE ? OR answer LIKE ?)"
        params.append(f"%{search}%")
        params.append(f"%{search}%")

    if category:
        query += " AND category = ?"
        params.append(category)

    query += " ORDER BY id DESC LIMIT ?"
    params.append(limit)

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data


def save_chat(user, bot):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)",
        (user, bot)
    )
    conn.commit()
    conn.close()


def get_chat_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_history ORDER BY id DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return data


def get_total_chats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM chat_history")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_total_categories():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT category) FROM faqs")
    count = cursor.fetchone()[0]
    conn.close()
    return count
