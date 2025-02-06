// Basic JavaScript Example: Alert on form submission
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for your message!');
});
