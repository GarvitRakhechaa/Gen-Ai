// Simple form handler for contact form
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

if (contactForm) {
  contactForm.addEventListener('submit', function(event) {
    event.preventDefault();
    formMessage.textContent = 'Thank you for reaching out! I will get back to you soon.';
    contactForm.reset();
  });
}
