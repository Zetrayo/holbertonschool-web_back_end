export default function getStudentsByLocation(List, City) {
    if (!Array.isArray(List))
      return [];
    const students = List.filter(student => student.location === City);
      return students;
}
