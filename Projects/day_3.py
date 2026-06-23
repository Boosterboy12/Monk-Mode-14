class identity:
    def __init__(self):
        pass

    def greet(name, age, profession):
        name = input("Enter You Name : ")
        age = int(input("Enter Your Age : "))
        profession = input(
            "Enter The Profession You Love FROM THE FOLLOWING : 1.Coder, 2. Developer, 3. Tech Enthusiast - "
        ).lower()
        print(
            f"Welcome {name} as you are a {profession} we would like you to answer the follwoing questions"
        )

    def qeustions(profession):
        if profession == "coder":
            language = input(
                "Please Select Any Language You Know From The Following :1.Java, 2. Python, 3. C, 4. C++ : "
            ).lower()
            if language == "java":
                print(
                    "Write Hello World In Java In all lower and uppercase where needed"
                )
                java_code = input("Enter The Code Here : ")

            elif language == "python":
                print(
                    "Write Hello World In Python In all lower and uppercase where needed"
                )
                python_code = input("Write Your Code Here : ")

            elif language == "c":
                print("Write Hello World In C In all lower and uppercase where needed")
                c_code = input("Write Your Code Here : ")

            elif language == "c++":
                print(
                    "Write Hello World In C++ In all lower and uppercase where needed"
                )
                c_plus_code = input("Write Your Code Here : ")

            else:
                print("Wrong Language Chosen")

        elif profession == "developer":
            developer_branch = input(
                "Select The Type Of Developer You Are : 1. Front End, 2. Back End, 3. Full Stack, 4. Niche"
            ).lower()
            if developer_branch == "front end" or "frontend":
                front_end_branch = input(
                    "Select Which Kind Of Front End Developer You Are : 1. UI/UX developer, 2. Front End Web Developer, 3. Mobile Front End Developer, 4. Static Developer ".lower()
                )
                if front_end_branch == "ui/ux" or "ui" or "ux" or "uiux" or "ui ux":
                    ui_ux_language = input(f"As You Are A {front_end_branch} Select The Language You Have Worked With From The Following")
                dev_language = input(
                    "Select The Language From The Following, You Have Worked With : 1. HTML, 2. CSS, 3. Javascript, ").lower()
                if front_end_branch == "front end web developer" or "frontend web developer" or "frontendwebdeveloper" or "front end webdeveloper" or "front end":
                    front_web_language = input(f"As You Are A {front_end_branch} Select Your Fav Languuage : 1. Javascript 2. TypeScript, 3. Vue.js, 4. React, 5. Angular ")

                if front_end_branch == "mobile front end dereloper" or "mobile frontend developer" or "mobilefrontenddeveloper" or "mobilefront end developer" or "mobiledrontend developer" or ""
  
            elif developer_branch == "back end" or "backend":           


vihaan = identity.greet("Vihaan", 13, "developer")
identity.qeustions("developer")
