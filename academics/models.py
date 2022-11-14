from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

"""
    All the database entities of users_app are described in this module.
"""

class Program(models.Model):
    """
     Program model represents different programs like BE Software, BE Civil, BE IT and so on.

     Each Program has its unique code.

     Each Program has different semesters; for master programs 4 semesters and for bachelor
     programs 8 semesters. Semester is represented by another model/table. Program and Semester
     has one-to-many relationship i.e One program has many semesters but particular semester
     belongs to only one program.
     """

    name = models.CharField(max_length=100)
    code = models.IntegerField()
    desc = models.TextField(default="", blank=True)

    def __str__(self):
        """
         :return: Readable representation of program object
        """
        return f'{self.name}'


    def get_absolute_url(self):
        """
        :return: url to the program specified by code as program/{code}
        """

        return reverse('programs', args=(self.code,))  # Displaying BE Software for all courses , should be changed



class Subject(models.Model):
    """
        Subject model represents the subjects of a particular semester/program.

        Each Subject has unique code.

        A semester has multiple subjects and similarly, a single subject, say Logic Circuit(Elx 110)
        belongs to 2nd Semester (of BE Software) and 3rd Semester (of BE IT) . So, Subject and Semester
        shows many-to-many relationship.

        Program and Subject are related through Semester. For example; if we want all the subjects of
        BE Software, then we have to retrieve each Semester of BE Software and from those individual semester,
        we can get the subjects.

        To ease the above process, we introduce the many-to-many relationship between Program and Subject.
        Now we can directly access the subjects of BE Software without joining Semester.

    """
    code = models.CharField(max_length=10, default='N/A')
    name = models.CharField(max_length=100)
    credit = models.IntegerField()
    programs = models.ManyToManyField(Program)

    def __str__(self):
        """
       :return: Readable representation of subject object
     """
        return f'{self.name}'



class Semester(models.Model):
    """
      Semester model represents the different semesters in the particular program.

      `sem` gives the semester  as 1, 2 , 3 and so on.

      Semester is related to Program model by a foreign key.

      Each Semester has different subjects related by field `subjects`.

    """
    sem = models.IntegerField(
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ])

    subjects = models.ManyToManyField(Subject)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)



    def get_meaningful_name(self):
        """
        :return: meaningful names for the given semester. Example, First(I) for 1, Second(II) for 2 and so on.
        """
        names = {
            1: "First (I)",
            2: "Second (II)",
            3: "Third (III)",
            4: "Fourth (IV)",
            5: "Fifth (V)",
            6: "Sixth (VI)",
            7: "Seventh (VII)",
            8: "Eight (VIII)"
        }
        return names.get(self.sem)


    def __str__(self):
        """
        :return: Readable representation of semester object
      """
        return f'{self.program} - {self.sem} sem'


class Grades(models.Model):
    roll = models.CharField(max_length=20)
    sem = models.IntegerField()
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    
    def __str__(self):
        return self.roll

class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.name
        
class Attendance(models.Model):
    roll = models.CharField(max_length=20)
    



