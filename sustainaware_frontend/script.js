function redirectToLogin() {
    window.location.href = "/Users/div910/Documents/SustainAware/sustainaware_frontend/login.html";
  }

  const button = document.querySelector('.button');

  button.addEventListener('click', function() {
    button.classList.toggle('active');
  });  
  