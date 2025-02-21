import Alpine from 'alpinejs';

window.Alpine = Alpine;

document.addEventListener('alpine:init', () => {
    Alpine.data('urlShortener', () => ({
        long_url: '',
        short_url: '',
        description: '',
        is_active: false,

        async generateShortURL() {
            const csrfToken = getCookie('csrftoken');

            const response = await fetch('/shorten/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    long_url: this.long_url,
                    description: this.description,
                    is_active: this.is_active
                })
            });

            const data = await response.json();
            if (response.ok) {
                this.short_url = window.location.origin + data.short_url;
            } else {
                console.error("Error:", data.error);
            }
        }
    }));
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

Alpine.start();