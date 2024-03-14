function minhafuncao1(){
    $('.btn-danger').empty().append('Novo nome');
    $('.btn-danger').css({
        color: '#00ff00',
        textTransform: 'uppercase',
        width: '70%'

    });
};

function minhafuncao2(){
    $('#area-mensagens').empty(); //Remove todos os elementos filhos daquele label

    var alunos = ['Aluno 01','Aluno 02','Aluno 03','Aluno 04','Aluno 05'];

    // Itera ao longo do array inserindo seus elementos ao final daquele cujo
    $.each(alunos, function(index, value) {
        $('#area-mensagens').append(value);
    });
};

function minhafuncao3(){
    $('.btn-danger').empty().append('Perigo');
    $('.btn-danger').css({
        color: '#ffffff',
        width: '5%'

    });
};