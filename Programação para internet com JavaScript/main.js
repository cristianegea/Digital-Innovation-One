function botao() {
    alert("Obrigado por clicar!!")
}

function clicou() {
    document.getElementById("agradecimento").innerHTML = "Obrigada por clicar!"  
    /*
    document.getElementById("agradecimento") => busca informação referente ao id="agradecimento" no HTML
    .innerHTML = "Obrigada por clicar!" => insere a mensagem na página
    .innerHTML => permite colocar qualquer coisa, não somente texto
    */
}

function redirecionamento() {
    window.open("https://www.globo.com/"); 
    /*
    window.open() => redireciona para uma outra página de internet
    window.open() => redireciona para uma outra página em uma outra aba/janela
    window.location.href = "https://..." => redireciona para uma outra página na mesma aba/janela
    */
}

function trocar() {
    alert("trocar texto!!!");
}

function trocarTexto() {
    document.getElementById("mousemove").innerHTML = "Obrigada por passar o mouse!";
}

function voltar() {
    document.getElementById("mousemove").innerHTML = "Passe o mouse aqui para mudar o texto";
}

function load() {
    alert("Página carregada!");
}

function functionChange(elemento) {
    console.log(elemento.value);
}

/*
// declaração de variáveis
var nome = "Cristiane";                         // variável tipo string
var number1 = 10;                               // variável tipo numérica
var number2 = number1 + 10;                     // variável tipo numérica
var frase ="O Japão é o melhor time do mundo";  // variável tipo string
var lista = ["maçã", "pêra", "laranja"];        // variável tipo lista
var fruta = {nome: "maça", cor: "vermelha"};    // variável tipo dicionário (aparência semelhante a um objeto .json)
var idade = 18;                                 // variável tipo numéica

// lista de dicionários
var frutas = [{nome: "maça", cor: "vermelha"}, {nome: "uva", cor: "roxa"}, {nome: "laranja", cor: "amarela"}];

// pop-up de alerta quando a página for carregada
alert("Bem vinda " + nome + "!");
    // no JavaScript, o sinal de + é utilizado para a concatenação de variáveis do tipo strings
alert(number2);
    // no JavaScript, o sinal de + pode ser utilizado para somar variáveis do tipo numéricas.

// execução no console do navegador
console.log(nome);
console.log(number1 + number2);
console.log(frase);
console.log(frase.replace("Japão", "Brasil"))   // substituição da palavra "Japão" pela palavra "Brasil"
console.log(frase.toLocaleUpperCase());         // coloca todas as letra em maiúsculo
console.log(frase.toLocaleLowerCase());         // coloca todas as letra em minúsculo
console.log(lista);
console.log(lista[0]);                          // acessa o elemento "maçã" da lista
console.log(lista[1]);                          // acessa o elemento "pêra" da lista
console.log(lista[2]);                          // acessa o elemento "laranja" da lista
lista.push("uva")                               // adiciona elemento no final da lista
console.log(lista);                 
lista.pop();                                    // retira o último elemento da lista
console.log(lista);
console.log(lista.length);                      // exibe a quantidade de elementos dentro da lista
console.log(lista.reverse());                   // inverte a ordem dos elementos em uma lista
console.log(lista.toString());                  // converte uma lista em uma string
console.log(lista.join(", "))                   // converte uma lista em uma string e permite inserir separadores entre as palavras
console.log(fruta.nome);                        // acessa o valor do atributo "nome"
console.log(fruta.cor);                         // acessa o valor do atributo "cor"
console.log(frutas);
console.log(frutas[0].nome);                    // acessa o valor do atributo "nome" do 1º elemento
console.log(frutas[1].nome);                    // acessa o valor do atributo "nome" do 2º elemento
console.log(frutas[2].nome);                    // acessa o valor do atributo "nome" do 3º elemento
console.log(frutas[0].cor);                     // acessa o valor do atributo "cor" do 1º elemento
console.log(frutas[1].cor);                     // acessa o valor do atributo "cor" do 2º elemento
console.log(frutas[2].cor);                     // acessa o valor do atributo "cor" do 3º elemento

// Condicional
if (idade > 18){
    console.log("é maior de idade");
} else {
    console.log("é menor de idade");
}

var anos = prompt("informe a sua idade");        // o usuário informa à máquina a idade
if (anos >= 18) {
    console.log("é maior de idade");
} else {
    console.log("é menor de idade");
}

// Laços de repetição
var count = 0                                       // definição do valor inicial da variável "count"

while (count <= 5){                                 // enquanto a declaração entre () for true, as instruções dentro de {} serão executadas
    console.log(count);
    count = count + 1;                              // é possível substituir por "count++"
}

for (count = 0; count <= 5; count++) {
    // "count = 0" => valor inicial da variável
    // "count <= 5" => enquanto a declaração entre () for true, as instruções dentro de {} serão executadas
    // "count++" => equivale a "count = count + 1"
    console.log(count);
}

// Datas
var d = new Date();
console.log(d);                                       // exibe a data atual (incluindo a hora)
console.log(d.getMonth() + 1);                        // exibe o mês atual (representação numérica, lembrando que janeiro = 0)
console.log(d.getDay());                              // exibe o dia da semana atual
console.log(d.getHours());                            // exibe a hora atual

// Funções
function sum(n1, n2) {                                // definição da função de soma
    return n1 + n2;                                   // o que eu quero que a função me retorne
}
console.log(sum(5, 10));                              // n1 = 5 e n2 = 10

function setReplace(frase, nome1, nome2) {            // definição da função de substituição
    return frase.replace(nome1, nome2);
}
console.log(setReplace("Vai Japão!", "Japão", "Brasil"));

function validaIdade(idade) {                          // definição da função de validação de idade
    var validar;                                       // variável local
    if (idade >= 18) {
        validar = true
    } else {
        validar = false
    }
    return validar;
}
var idade = prompt("informe a sua idade");
console.log(validaIdade(idade));

var validar;                                            // variável global
function validaIdade(idade) {                           // outra forma de definir a função de validação de idade
    validar;
    if (idade >= 18) {
        validar = true
    } else {
        validar = false
    }
    return validar;
}
var idade = prompt("informe a sua idade");
validaIdade(idade);
console.log(validar);
*/