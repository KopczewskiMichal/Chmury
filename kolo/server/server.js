const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

const logDirectory = path.join(__dirname, 'logs');
if (!fs.existsSync(logDirectory)) {
  fs.mkdirSync(logDirectory);
}

const logFilePath = path.join(logDirectory, 'app.log');

function log(message) {
  const timestamp = new Date().toISOString();
  const logMessage = `${timestamp} - ${message}\n`;

  // Zapisywanie logu do pliku
  fs.appendFile(logFilePath, logMessage, (err) => {
    if (err) {
      console.error('Error writing to log file', err);
    }
  });

  // Wyświetlanie logu w konsoli
  console.log(logMessage);
}

// Middleware do logowania każdego żądania
app.use((req, res, next) => {
  log(`${req.method} ${req.path}`);
  next();
});