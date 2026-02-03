// Función para cerrar alertas automáticamente después de 5 segundos
document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(function(alert) {
        setTimeout(function() {
            // Verificamos que Bootstrap esté disponible para evitar errores
            if (typeof bootstrap !== 'undefined' && bootstrap.Alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } else {
                // Alternativa si Bootstrap JS no cargó: ocultar con CSS
                alert.style.display = 'none';
            }
        }, 5000);
    });
});