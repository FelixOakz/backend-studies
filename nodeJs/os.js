const { exec } = require('child_process');

exec('ls', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        return;
    }
    console.log('List of Files:', stdout);
});
