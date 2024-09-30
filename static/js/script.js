// Contact Form Submission
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Simple form validation
    if (name && email && message) {
        alert('Thank you for contacting us, ' + name + '!');
        document.getElementById('contactForm').reset();
    } else {
        alert('Please fill out all fields.');
    }
});
