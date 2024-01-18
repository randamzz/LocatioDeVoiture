function hideLabels() {
    var labels = document.querySelectorAll('label');
    labels.forEach(function(label) {
        label.style.display = 'none';
    });
}
window.onload = hideLabels;document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("myForm");
    var submitBtn = document.getElementById("submitBtn");
    var emailField = document.getElementById("email");
    var emailError = document.getElementById("emailError");
    var numeroField = document.getElementById("numero");
    var numeroError = document.getElementById("numeroError");
    var dateDebutField = document.getElementById("date_debut");
    var dateFinField = document.getElementById("date_fin");

    form.addEventListener("input", function () {
        // Check if all input fields have a value
        var allFieldsFilled = true;

        form.querySelectorAll("input").forEach(function (input) {
            if (input.value.trim() === "") {
                allFieldsFilled = false;
            }
        });

        // Enable/disable the submit button based on the condition
        submitBtn.disabled = !allFieldsFilled;
    });

    // Email format validation
    emailField.addEventListener("input", function () {
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailField.value)) {
            emailError.textContent = "Invalid email format";
        } else {
            emailError.textContent = "";
        }
        checkFormValidity();
    });

    // Numero format validation
    numeroField.addEventListener("input", function () {
        var numeroRegex = /^\d+$/;
        if (!numeroRegex.test(numeroField.value)) {
            numeroError.textContent = "Invalid numero format (only digits allowed)";
        } else if (numeroField.value.length < 10) {
            numeroError.textContent = "Minimum 10 digits required";
        } else {
            numeroError.textContent = "";
        }
        checkFormValidity();
    });

    function checkFormValidity() {
        // You can add additional checks or logic here if needed
    }
});
document.addEventListener("DOMContentLoaded", function () {
    // Fonction pour obtenir la date actuelle au format "YYYY-MM-DD"
    function getCurrentDate() {
        var currentDate = new Date();
        var year = currentDate.getFullYear();
        var month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
        var day = currentDate.getDate().toString().padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    // Fonction pour désactiver les dates antérieures
    function disablePastDates(dateField) {
        var currentDate = getCurrentDate();

        // Définir l'attribut min pour la date de début et de fin
        dateField.min = currentDate;

        // Ajouter un écouteur d'événements pour gérer les modifications de la date de début
        dateField.addEventListener("input", function () {
            // Valider la date sélectionnée par rapport à la date minimale
            if (dateField.value < currentDate) {
                dateField.setCustomValidity("Veuillez sélectionner une date aujourd'hui ou ultérieure");
            } else {
                dateField.setCustomValidity("");
            }
        });
    }

    // Obtenez les champs de date de début et de fin
    var dateDebutField = document.getElementById("id_date_debut");  // Assurez-vous que l'ID est correct
    var dateFinField = document.getElementById("id_date_fin");  // Assurez-vous que l'ID est correct

    // Désactiver les dates antérieures pour les champs de date de début et de fin
    if (dateDebutField) {
        disablePastDates(dateDebutField);
    }

    if (dateFinField) {
        disablePastDates(dateFinField);
    }
});

//ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
// Assurez-vous que le DOM est chargé avant d'exécuter le script
document.addEventListener("DOMContentLoaded", function () {
    function getCurrentDate() {
        var currentDate = new Date();
        var year = currentDate.getFullYear();
        var month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
        var day = currentDate.getDate().toString().padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    function disablePastDates(dateField) {
        var currentDate = getCurrentDate();
        dateField.min = currentDate;
        dateField.addEventListener("input", function () {
            if (dateField.value < currentDate) {
                dateField.setCustomValidity("Veuillez sélectionner une date aujourd'hui ou ultérieure");
            } else {
                dateField.setCustomValidity("");
            }
        });
    }

    var dateDebutField = document.getElementById("date_debut");
    var dateFinField = document.getElementById("date_fin");

    if (dateDebutField) {
        disablePastDates(dateDebutField);
    }

    if (dateFinField) {
        disablePastDates(dateFinField);
    }
});
