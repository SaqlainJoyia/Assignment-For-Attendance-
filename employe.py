class Employee:
    def init(self, employee_id, name):
        self.employee_id = employee_id
        self.name = "noman"
        self.attendance_records = []
        self.salary = 0
        

    def add_attendance_record(self, date, time_in, time_out):
        self.attendance_records.append(Attendance(date, time_in, time_out))

    def remove_attendance_record(self, date):
        for record in self.attendance_records:
            if record.date == date:
                self.attendance_records.remove(record)

    def get_attendance_records(self):
        return self.attendance_records

    def calculate_salary(self, hourly_rate):
        total_hours = 0
        for record in self.attendance_records:
            total_hours += record.calculate_hours()
        self.salary = Salary(hourly_rate, total_hours).calculate_salary()

class Attendance:
    def init(self, date, time_in, time_out):
        self.date = date
        self.time_in = time_in
        self.time_out = time_out

    def calculate_hours(self):
        return (self.time_out - self.time_in).total_seconds() / 3600


class Salary:
    def init(self, hourly_rate, total_hours):
        self.hourly_rate = hourly_rate
        self.total_hours = total_hours
        self.total_pay = 0
        
    def calculate_salary(self):
        self.total_pay = self.hourly_rate * self.total_hours
        return self.total_pay