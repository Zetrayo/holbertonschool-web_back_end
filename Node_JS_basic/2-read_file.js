const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf-8');
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        if (lines.length < 2) {
            throw new Error('Cannot load the database');
        }
        const header = lines[0].split(',');
        const students = lines.slice(1).map((line) => line.split(','));
        console.log(`Number of students: ${students.length}`);
        const fields = {};
        students.forEach((student) => {
            const field = student[3];
            const firstname = student[0];
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });
        for (const [field, firstnames] of Object.entries(fields)) {
            console.log(
                `Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`
            );
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
