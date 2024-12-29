document.getElementById("signup-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const formData = {
    email: email,
    password: password,
  };

  console.log("Form data:", formData);
  // Here you would typically send the data to your server
  // For demonstration purposes, we're just logging it to the console
});
