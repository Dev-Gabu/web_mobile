function minhafuncao1(){
    alert('Minha função');
};

function minhafuncao(){
    $('#area-mensagens').empty(); //Remove todos os elementos filhos daquele label

    var alunos = ['Aluno 01','Aluno 02','Aluno 03','Aluno 04','Aluno 05'];

    // Itera ao longo do array inserindo seus elementos ao final daquele cujo
    $.each(alunos, function(index, value) {
        $('#area-mensagens').append(value)
    })
};