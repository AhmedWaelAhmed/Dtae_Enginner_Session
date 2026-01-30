-- 1. إنشاء جدول بخصائص Postgres (SERIAL + TEXT)

DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    ID SERIAL PRIMARY KEY,
    Name TEXT NOT NULL,
    EnrollmentDate TIMESTAMP DEFAULT NOW()
);

-- 2. إدخال بيانات (بدون تحديد الـ ID لأنه تلقائي)
INSERT INTO Students (Name) VALUES 
    ('Ahmed'), 
    ('Sara'), 
    ('Ali');

-- 3. عرض أول صفين فقط (LIMIT بدلاً من TOP)
SELECT * FROM Students LIMIT 2;

-- 4. عرض التوقيت الحالي
SELECT NOW();