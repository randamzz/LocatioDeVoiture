function hideLabels() {
    var labels = document.querySelectorAll('label');
    labels.forEach(function(label) {
        label.style.display = 'none';
    });
}
window.onload = hideLabels;