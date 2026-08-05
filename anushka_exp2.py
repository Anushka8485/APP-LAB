def report_format(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("        DYNAMIC REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
        print("          END OF REPORT")
        print("=" * 40)
    return wrapper


class Report:
    def __init__(self, title):
        self.title = title
        self.sections = []

    def add_section(self, heading, content):
        self.sections.append((heading, content))

    @classmethod
    def create_template(cls):
        report = cls("Student Performance Report")
        report.add_section("Introduction", "This report shows student performance.")
        report.add_section("Conclusion", "Overall performance is satisfactory.")
        return report

    def __str__(self):
        output = f"\nReport Title: {self.title}\n\n"
        for heading, content in self.sections:
            output += f"{heading}\n"
            output += f"{content}\n\n"
        return output

    def __len__(self):
        return len(self.sections)


class Formatter:

    @staticmethod
    @report_format
    def display(report):
        print(report)
        print("Total Sections:", len(report))


report = Report.create_template()

report.add_section("Marks", "Python = 90\nJava = 85\nDBMS = 88")
report.add_section("Attendance", "Attendance = 95%")

Formatter.display(report)