CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    date_created TEXT,
    hire_date TEXT,
    active INTEGER DEFAULT 1,
    manager INTEGER 
);


CREATE TABLE IF NOT EXISTS Competencies(
    comp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    comp_name TEXT,
    date_created TEXT
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_name TEXT,
    comp_id INTEGER,
    date_created TEXT,
    FOREIGN KEY (comp_id)
        REFERENCES Competencies(comp_id)
);

CREATE TABLE IF NOT EXISTS Results(
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    assessment_id TEXT,
    comp_score TEXT,
    date_taken TEXT,
    admin_id INTEGER,
    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),
    FOREIGN KEY (assessment_id)
        REFERENCES Assessments(assessment_id),
    FOREIGN KEY (admin_id)
        REFERENCES Users(user_id)
);