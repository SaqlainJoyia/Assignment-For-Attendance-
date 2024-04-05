class Vehicle:
    def __init__(self, plate_number, driver_name):
        self.plate_number = plate_number
        self.driver_name = driver_name
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True

    def __str__(self):
        return f"Plate Number: {self.plate_number}, Driver Name: {self.driver_name}, Attendance: {'Present' if self.attendance else 'Absent'}"


class VehicleTracker:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, plate_number, driver_name):
        vehicle = Vehicle(plate_number, driver_name)
        self.vehicles.append(vehicle)

    def mark_attendance(self, plate_number):
        for vehicle in self.vehicles:
            if vehicle.plate_number == plate_number:
                vehicle.mark_attendance()
                print(f"Attendance marked for vehicle with plate number {plate_number}.")
                return
        print(f"Vehicle with plate number {plate_number} not found.")

    def display_attendance(self):
        for vehicle in self.vehicles:
            print(vehicle)


# Example usage:
tracker = VehicleTracker()

# Adding vehicles
tracker.add_vehicle("ABC123", "saqlian")
tracker.add_vehicle("XYZ789", "marva")

# Marking attendance
tracker.mark_attendance("ABC123")

# Displaying attendance
tracker.display_attendance()
