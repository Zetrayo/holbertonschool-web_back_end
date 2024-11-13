export default function createReportObject(employeesList) {
    const a = {
        allEmployees: employeesList,
        getNumberOfDepartments: function() {
            return Object.keys(this.allEmployees).length;
        }
    };
    return a
}
