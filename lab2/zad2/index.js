const http = require("http");

const hostname = "0.0.0.0";
const port = 8080;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  const options = {
    timeZone: 'Europe/Warsaw',
    hour12: false,
    weekday: 'long', 
    year: 'numeric',
    month: 'long', 
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric'
  };
  const currentDate = new Date();
  res.end(`Hello World\nObecna data to: ${currentDate.toLocaleString('pl-PL', options)}`);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});