function showCars(category) {
    // Hide all cars
    document.querySelectorAll('.car-item').forEach(function(car) {
        car.style.display = 'none';
    });

    // Show cars based on the selected category
    if (category !== 'all') {
        document.querySelectorAll('.' + category + '-car').forEach(function(car) {
            car.style.display = 'block';
        });
    } else {
        // If 'All Cars' is selected, show all cars
        document.querySelectorAll('.car-item').forEach(function(car) {
            car.style.display = 'block';
        });
    }
}