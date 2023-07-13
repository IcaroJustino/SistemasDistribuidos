const express = require('express');
const path = require('path');

const app = express()
const server = require('http').createServer(app);  //conexão utilizando websocket wss
const io = require('socket.io')(server);  //conexão utilizando websocket wss


app.use(express.static(path.join(__dirname,'public'))); //definição da pasta statica do express para renderizar o html (client)

app.set('views',path.join(__dirname,'public'));  //entender que as views são html e não ejs

app.engine('html',require('ejs').renderFile); //entender que as views são html e não ejs

app.set('view engine','html');

app.use('/',(req,res) => { //para ele renderizar o servidor padrão e mostrar o html
    res.render('index.html');
}
);

let messages = []; // mensagens antigas

io.on('connection', (socket) => {
    console.log(`someone connected! ${socket.id}`);

    socket.emit('previousMessages',messages)

    socket.on('sendMessage',(data) =>{
        console.log(data)
        messages.push(data);

        socket.broadcast.emit('receivedMessage',data)
    })
  });

server.listen(3000)
