function clearAllOptions() {
    if (confirm('Are you sure you want to clear all options?')) {
        window.location.href = "/delete-all-options";
    }
}

function clearAllParticipants() {
    if (confirm('Are you sure you want to clear all participants?')) {
        window.location.href = "/delete-all-participants";
    }
}