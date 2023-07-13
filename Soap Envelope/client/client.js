const soap = require('soap');

const wsdlUrl = 'http://127.0.0.1:8000/?wsdl'; // URL do servidor SOAP

// Função para fazer uma chamada retornar todos os monstros 
function getAllMonsters() {
  soap.createClient(wsdlUrl, function(err, client) {
    if (err) {
      console.error('Erro ao criar o cliente SOAP:',err);
      return;
    }

    client.get_all_monsters(function(err, result) {
      if (err) {
        console.error('Erro ao chamar o método getAllMonsters:', err);
        return;
      }

      console.log('Monstros:', result);
    });
  });
}

// Função para fazer uma chamada  e retornar um monstro 
function getMonster(monsterId) {
  soap.createClient(wsdlUrl, function(err, client) {
    if (err) {
      console.error('Erro ao criar o cliente SOAP:', err);
      return;
    }

    client.get_monster({ monster_id: monsterId }, function(err, result) {
      if (err) {
        console.error('Erro ao chamar o método getMonster:', err);
        return;
      }

      console.log('Monstro:', result);
    });
  });
}

// Função para fazer uma chamada e retornar todos os items
function getAllItems() {
  soap.createClient(wsdlUrl, function(err, client) {
    if (err) {
      console.error('Erro ao criar o cliente SOAP:', err);
      return;
    }

    client.get_all_items(function(err, result) {
      if (err) {
        console.error('Erro ao chamar o método getAllItems:', err);
        return;
      }

      console.log('Itens:', result);
    });
  });
}

// Função para fazer uma e retornar um item
function getItem(itemId) {
  soap.createClient(wsdlUrl, function(err, client) {
    if (err) {
      console.error('Erro ao criar o cliente SOAP:', err);
      return;
    }

    client.get_item({ item_id: itemId }, function(err, result) {
      if (err) {
        console.error('Erro ao chamar o método getItem:', err);
        return;
      }

      console.log('Item:', result);
    });
  });
}

// Exemplo de uso
const endpoint = process.argv[2]; // Argumento da linha de comando para selecionar o endpoint

if (endpoint === 'all_monsters') {
  getAllMonsters();
} else if (endpoint === 'monster') {
  const monsterId = process.argv[3]; // Argumento da linha de comando para o ID do monstro
  getMonster(monsterId);
} else if (endpoint === 'all_items') {
  getAllItems();
} else if (endpoint === 'item') {
  const itemId = process.argv[3]; // Argumento da linha de comando para o ID do item
  getItem(itemId);
} else {
  console.error('Endpoint inválido!');
}