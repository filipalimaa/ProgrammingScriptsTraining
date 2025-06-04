// Adiciona token anti-CSRF ao formulário antes de enviar
$(document).ready(function() {
    var csrfToken = document.querySelector('input[name="csrf_token"]').value;
    $('#loginForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        // username=bruno&password=123456
        formData += '&csrf_token=' + csrfToken; // Adiciona o token ao formulário
        // username=bruno&password=123456&csrf_token=abc123456
        $.ajax({
            type: 'POST',
            url: '/login',
            data: formData,
            success: function(response) {
                alert('Login bem-sucedido!');
                window.location.href = '/dashboard';
            },
            error: function(xhr, status, error) {
                alert('Erro ao fazer login.');
            }
        });
    });
});


