export default function getListStudentIds(List) {
  if (!Array.isArray(List))
    return [];
  const ids = List.map(student => student.id);
    return ids;
}
