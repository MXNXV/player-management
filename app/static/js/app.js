document.addEventListener("DOMContentLoaded", function(){
    const actionButtons = document.querySelectorAll('form button[data-action]');
    actionButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            let action = button.getAttribute('data-action');
            // let message = "Are you sure you want to perform this action?";
            if (action === "delete") {
                message = "Are you sure you want to delete this player?";
            } else if (action === "update") {
                message = "Are you sure you want to update this player's information?";
            } else if (action === "add") {
                message = "Are you sure you want to add a new player?";
            }

            if (!confirm(message)) {
                event.preventDefault();
            }
        });
    });
});
