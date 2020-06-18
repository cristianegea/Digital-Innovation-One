// Requisição Ajax utilizando biblioteca JQuery
function consultaCep() {
    $(".barraprogresso").show();    // Exibição do conteúdo da classe "cep" quando é realizada uma nova consulta
    var cep = document.getElementById("cep").value;
    var url = "http://viacep.com.br/ws/" + cep + "/json/"
    console.log (cep);
    // função do JQuery
    $.ajax({
        // url da requisição
        url: url,                               
        // GET = tipo de requisição
        type: "GET",
        // caso a requisição ocorra com sucesso, a função "response" será executada                                        
        success: function(response) {
            console.log(response);              // output: objeto tipo dicionário com todos os dados
            // console.log(response.bairro) => output = bairro
            // console.log(response.logradouro) => output = logradouro
            
            // Extração de cada componente do dicionário
            $("#titulocep").html("Cep: " + response.cep);
            $("#bairro").html(response.bairro);
            $("#complemento").html(response.complemento);
            $("#localidade").html(response.localidade);
            $("#logradouro").html(response.logradouro);
            $("#uf").html(response.uf);
            $(".cep").show();       // Exibição do conteúdo da classe "cep" quando é realizada uma nova consulta
            $(".barraprogresso").hide(); // oculta o conteúdo da classe depois que a pesquisa é finalizada
            /*
            Outra forma de fazer:
            document.getElementById("bairro").innerHTML = response.bairro;
            document.getElementById("cep").innerHTML = response.cep;
            document.getElementById("complemento").innerHTML = response.complemento;
            document.getElementById("localidade").innerHTML = response.localidade;
            document.getElementById("logradouro").innerHTML = response.logradouro;
            document.getElementById("uf").innerHTML = response.uf;
            */
        }
        
    })    
}

// Oculta todo o conteúdo das classes "cep" e "barraprogresso"
$(function(){
    $(".cep").hide();
    $(".barraprogresso").hide();
});

