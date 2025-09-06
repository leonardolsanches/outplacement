// Plataforma Outplacement - Main JavaScript

// Initialize when document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert-dismissible');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Add loading animation to buttons on click
    var buttons = document.querySelectorAll('button[type="submit"]');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            if (this.form && this.form.checkValidity()) {
                addLoadingToButton(this);
            }
        });
    });
});

// Add loading animation to button
function addLoadingToButton(button) {
    var originalText = button.innerHTML;
    button.innerHTML = '<span class="loading me-2"></span>Processando...';
    button.disabled = true;
    
    // Re-enable button after 3 seconds (fallback)
    setTimeout(function() {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 3000);
}

// Utility functions for API calls
function showAlert(message, type = 'info') {
    var alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    var container = document.querySelector('.container-fluid');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(function() {
        var alert = new bootstrap.Alert(alertDiv);
        alert.close();
    }, 5000);
}

// Format date strings
function formatDate(dateString) {
    var date = new Date(dateString);
    return date.toLocaleDateString('pt-BR');
}

// Format datetime strings
function formatDateTime(dateString) {
    var date = new Date(dateString);
    return date.toLocaleDateString('pt-BR') + ' ' + date.toLocaleTimeString('pt-BR', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Validate form fields
function validateForm(form) {
    var isValid = true;
    var inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    
    inputs.forEach(function(input) {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    });
    
    return isValid;
}

// Clear form validation classes
function clearFormValidation(form) {
    var inputs = form.querySelectorAll('.is-valid, .is-invalid');
    inputs.forEach(function(input) {
        input.classList.remove('is-valid', 'is-invalid');
    });
}

// Generic API call function
async function apiCall(url, method = 'GET', data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        }
    };
    
    if (data) {
        options.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(url, options);
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('API Error:', error);
        showAlert('Erro na comunicação com o servidor', 'danger');
        return null;
    }
}

// Confirm dialog for destructive actions
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Update progress bar
function updateProgressBar(element, percentage) {
    element.style.width = percentage + '%';
    element.textContent = percentage + '%';
}

// Dashboard utilities
function updateDashboardStats() {
    // This would typically fetch real-time stats from the API
    // For now, it's a placeholder for future implementation
    console.log('Updating dashboard statistics...');
}

// Session management
function scheduleSession(executiveId, date, time) {
    const sessionData = {
        executive_id: executiveId,
        date: date,
        time: time,
        status: 'scheduled'
    };
    
    apiCall('/api/sessions', 'POST', sessionData)
        .then(result => {
            if (result && result.success) {
                showAlert('Sessão agendada com sucesso!', 'success');
                location.reload();
            } else {
                showAlert('Erro ao agendar sessão', 'danger');
            }
        });
}

// Generate report
function generateReport(type, period) {
    const params = new URLSearchParams({
        type: type,
        period: period
    });
    
    window.open(`/api/reports?${params}`, '_blank');
}