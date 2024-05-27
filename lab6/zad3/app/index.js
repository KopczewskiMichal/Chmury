const express = require('express');
const { MongoClient } = require('mongodb');

const app = express();
const port = 3000;

const mongoUrl = 'mongodb://mongo:27017';
const dbName = 'myDatabase';

app.get('/', async (req, res) => {
    let client;

    try {
        client = new MongoClient(mongoUrl, { useUnifiedTopology: true });
        await client.connect();

        console.log('Połączono z MongoDB');
        const db = client.db(dbName);
        const kolekcja = db.collection('myCollection');

        const dane = await kolekcja.find({}).toArray();
        res.json(dane);
    } catch (err) {
        console.error('Błąd podczas łączenia z MongoDB', err);
        res.status(500).send('Błąd serwera');
    } finally {
        if (client) {
            await client.close();
        }
    }
});

app.listen(port, () => {
    console.log(`Serwer działa na porcie ${port}`);
});
