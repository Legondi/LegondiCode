const express = require('express');
const { it } = require('node:test');
const app = express();
const port = 3000;

app.use(express.json());

let itens = [
    { id: 1, name: "Engenharia de Software"},
    { id: 2, name: "Sistemas de Informacao"}
];

app.get('/itens', (req, res) => {
 res.status(200).json(itens);
});

app.post('/itens', (req, res) =>  {

    const newItem = {id: itens.length + 1, name: req.body.name}
    itens.push(newItem);
    res.status(201).json(newItem);

});

app.listen(port, () => {
    console.log(`Servidor está rodando em http://localhost:${port}`);
});