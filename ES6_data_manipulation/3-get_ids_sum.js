export default function getStudentIdsSum (List) {
    if (!Array.isArray(List))
      return 0;
    const idSum = List.reduce((idval, idval1) => idval + idval1.id, 0);
      return idSum;
}
