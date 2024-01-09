//search selon categorie 
function filterCarsByCategory(category) {
    var cars = document.querySelectorAll('.fruite-item');
    cars.forEach(function(car) {
        var carCategories = car.className.split(' ').filter(function(className) {
            return className !== 'fruite-item';  // Retirez la classe principale
        });
        if (category === 'all' || carCategories.includes(category)) {
            car.style.display = 'block';
        } else {
            car.style.display = 'none';
        }
    });
}
document.getElementById('fruits').addEventListener('change', function() {
    var selectedCategory = this.value;
    filterCarsByCategory(selectedCategory);
});
filterCarsByCategory(document.getElementById('fruits').value);

//selon prix 
function updatePriceFilter(selectedPrice) {
document.getElementById('amount').textContent = selectedPrice + " MAD";
var cars = document.querySelectorAll('.fruite-item');
cars.forEach(function(car) {
    var carPrice = parseFloat(car.dataset.price);
    if (carPrice < selectedPrice) {
        car.style.display = 'block'; 
    } else {
        car.style.display = 'none';   
    }
});
}

// Pagination 

