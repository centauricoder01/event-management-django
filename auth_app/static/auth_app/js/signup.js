// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("signup-form");

//   form.addEventListener("submit", function (e) {
//     e.preventDefault();

//     const name = document.getElementById("name").value;
//     const email = document.getElementById("email").value;
//     const organization = document.getElementById("organization").value;
//     const password = document.getElementById("password").value;

//     const formData = {
//       name: name,
//       email: email,
//       organization: organization,
//       password: password,
//     };

//     console.log("Form data:", formData);

//     form.reset();
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("signup-form");
  const responseMessage = document.getElementById("response-message");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      headers: {
        "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
      },
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          responseMessage.textContent = data.message;
          responseMessage.style.color = "green";
          form.reset();
        } else {
          responseMessage.textContent =
            "Errors: " + JSON.stringify(data.errors);
          responseMessage.style.color = "red";
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
