export default function createEmployeesObject(departmentName, employees) {
    const all = {
        [`${departmentName}`]: [`${employees.join(', ')}`],
   }
    return all
}
