class MarksDescriptor:
    def __get__(self, obj, objtype):
        return obj._marks

    def __set__(self, obj, value):
        for mark in value:
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100")
        obj._marks = value


class SalaryDescriptor:
    def __get__(self, obj, objtype):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj._salary = value
