const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }
            try {
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
                resolve();
            } catch (error) {
                reject(new Error('Cannot load the database'));
            }
        });
    });
}

module.exports = countStudents;
