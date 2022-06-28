function requestUrl(url) {
    $.ajax({
        url: url,
        success: function(data) {
            console.log('sucesso')
        }
    });

}

function load_cadastro() {
    window.location.href = "/"
}

function remover_usuario(user_id) {
    let url = `/remover_usuario/${user_id}`
    response = requestUrl(url)
    window.location.reload();
}

function editar_usuario(user_id) {
    let url = `/editar/${user_id}`
    window.location.href = url
}

$('.deletar').click(function() {
    let user_id = $(this).parent().parent().find(".id").html();
    remover_usuario(user_id)
})

$('.editar').click(function() {
    let user_id = $(this).parent().parent().find(".id").html();
    editar_usuario(user_id)
})