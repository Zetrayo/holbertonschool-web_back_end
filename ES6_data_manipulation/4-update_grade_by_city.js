export default function updateStudentGradeByCity(List, City, NewGrades) {
  if (!Array.isArray(List))
    return [];
  const studentsInCity = List.filter(student => student.location === City);
  const updatedStudents = studentsInCity.map(student => {
    const gradeUpdate = NewGrades.find(grade => grade.studentId === student.id)
    return {...student, grade: gradeUpdate ? gradeUpdate.grade : "N/A"
  };
});
  return updatedStudents;
}
