import requests

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://calms.pythonanywhere.com/reporter/attempt/"
    
    def checking(self, tg_username, isSolved, homework_name):
        data = {
            "tg_username": tg_username,
            "assignment_name": homework_name,
            "task_name": self.task_name,
            "is_correct": isSolved
        }
        response = requests.post(self.url, data=data)
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)
    

# A integer type variable 'number' is given. Return the absolute value of a "number".
class TaskOne(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(5) == 5
    
    def test_case_2(self, solution):
        return solution(-5) == 5
    
    def test_case_3(self, solution):
        return solution(0) == 0
    
    def test_case_4(self, solution):
        return solution(-2.5) == 2.5
    

    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)


# -2.55
class TaskTwo(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution() == -2.55
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)

# A integer type variable 'n' is given. Return the value of the expression: 3(n+1)^{2}
class TaskThree(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(3.5) == 60.75
    
    def test_case_2(self, solution):
        return solution(-2.5) == 6.75
    
    def test_case_3(self, solution):
        return solution(0) == 3
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)


# A integer type variable 'n' is given. Return the value of the expression: \frac{2+n}{3})^{2}
class TaskFour(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(3.5) == 3.3611111111111107
    
    def test_case_2(self, solution):
        return solution(-2.55) == 0.033611111111111085
    
    def test_case_3(self, solution):
        return solution(4) == 4.0
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)

# Integer type variables 'n' and 'x' are given. Return the value of the expression:  \(x^{n}+n^{x})

class TaskFive(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(5, 3.2) == 508.01052768265197
    
    def test_case_2(self, solution):
        return solution(2, 2) == 8
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1,
            self.test_case_2
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)

# Float type variables 'a' is given. Round the result to 2 decimal places Use the `round()` function

class TaskSix(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(5.555) == 5.56
    
    def test_case_2(self, solution):
        return solution(2.222) == 2.22
    
    def test_case_3(self, solution):
        return solution(0) == 0.0
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)


# Integer type variables 'x' and 'y' are given. Return the value of the expression: \(x^{2}+6x^{3}+3xy)

class TaskSeven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(5, 9) == 910
    
    def test_case_2(self, solution):
        return solution(1.25, 4.5) == 28.28125
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)

# example: x = 7, y = 1, answer = 252, x = 2, y = 2.46, answer = 309.84191999999996
class TaskEight(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(7, 1) == 252
    
    def test_case_2(self, solution):
        return solution(2, 2.46) == 309.84191999999996
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)

# example x = 5, y = 10, answer = 2500, x = 2.5, y = 4.5, answer = 238.5, x = 10, y = 9.5, answer = 3614.75

class TaskNine(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(5, 10) == 2500
    
    def test_case_2(self, solution):
        return solution(2.5, 4.5) == 238.5
    
    def test_case_3(self, solution):
        return solution(10, 9.5) == 3614.75
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)

# exapmple x = 3.14, y = 4 answer = 8.1, x = 20, y = 5.5, answer = 14.4

class TaskTen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(3.14, 4) == 8.1
    
    def test_case_2(self, solution):
        return solution(20, 5.5) == 14.4
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution)
        ]
        isSolve = all(test_cases)
        self.checking(tg_username, isSolve, self.homework_name)


q1 = TaskOne('build_func01', "	build_in_function")
q2 = TaskTwo('build_func02', "	build_in_function")
q3 = TaskThree('build_func03', "	build_in_function")
q4 = TaskFour('build_func04', "	build_in_function")
q5 = TaskFive('build_func05', "	build_in_function")
q6 = TaskSix('build_func06', "	build_in_function")
q7 = TaskSeven('build_func07', "	build_in_function")
q8 = TaskEight('build_func08', "	build_in_function")
q9 = TaskNine('build_func09', "	build_in_function")
q10 = TaskTen('build_func10', "	build_in_function")
