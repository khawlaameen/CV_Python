class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date
    
    def display_experience(self):
        print("Company: ", self.company)
        print("Job Title: ", self.job_title)
        print("Start Date: ", self.start_date)
        print("End Date: ", self.end_date)

class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date
    
    def display_education(self):
        print("Degree: ", self.degree)
        print("Institution: ", self.institution)
        print("Completion Date: ", self.completion_date)

class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage
    
    def display_skill(self):
        print("Skill: ", self.skill)
        print("Percentage: ", self.percentage)

class CV:
    def __init__(self):
        self.experiences = []
        self.education = []
        self.skills = []
    
    def add_experience(self):
        company = input("Enter company name: ")
        job_title = input("Enter job title: ")
        start_date = input("Enter start date: ")
        end_date = input("Enter end date: ")
        
        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)
        
        choice = input("Do you want to add another experience? (yes/no): ")
        if choice.lower() == "yes":
            self.add_experience()
    
    def add_education(self):
        degree = input("Enter your degree: ")
        institution = input("Enter your institution: ")
        completion_date = input("Enter completion date: ")
        
        education = Education(degree, institution, completion_date)
        self.education.append(education)
        
        choice = input("Do you want to add another education? (yes/no): ")
        if choice.lower() == "yes":
            self.add_education()
    
    def add_skill(self):
        skill = input("Enter skill: ")
        percentage = input("Enter percentage: ")
        
        skill = Skill(skill, percentage)
        self.skills.append(skill)
        
        choice = input("Do you want to add another skill? (yes/no): ")
        if choice.lower() == "yes":
            self.add_skill()
    
    def display_cv(self):
        print("\n Your CV\n")
        print("Name:\n ", self.name)
        
        print("\n* Experiences:\n")
        for experience in self.experiences:
            experience.display_experience()
        
        print("\n* Education:\n")
        for education in self.education:
            education.display_education()
        
        print("\n* Skills:\n")
        for skill in self.skills:
            skill.display_skill()



cv = CV()
cv.name = input("Enter your name: ")

choice = input("Do you want to add skills? (yes/no): ")
if choice.lower() == "yes":
    cv.add_skill()
    
choice = input("Do you want to add education ? (yes/no): ")
if choice.lower() == "yes":
   cv.add_education()

choice = input("Do you want to add experience ? (yes/no): ")
if choice.lower() == "yes":
   cv.add_experience()

cv.display_cv()

