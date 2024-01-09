let itemsPerPage = 6;
let page = 1;
const nextButton = document.getElementById('next-btn');
const prevButton = document.getElementById('prev-btn');
const cars = document.querySelectorAll('.fruite-item');

const updateCarsVisibility = (category) => {
  let visibleCarsCount = 0;

  cars.forEach((car, index) => {
    const carCategories = car.className.split(' ').filter(className => className !== 'fruite-item');

    if (category === 'all' || carCategories.includes(category)) {
      const isVisible = visibleCarsCount >= (page - 1) * itemsPerPage && visibleCarsCount < page * itemsPerPage;
      car.style.display = isVisible ? 'block' : 'none';
      visibleCarsCount++;
    } else {
      car.style.display = 'none';
    }
  });
};

updateCarsVisibility(document.getElementById('fruits').value);

document.getElementById('fruits').addEventListener('change', function() {
  const selectedCategory = this.value;
  page = 1; // Reset the page when changing the category
  updateCarsVisibility(selectedCategory);
});

nextButton.addEventListener('click', () => {
  page++;
  updateCarsVisibility(document.getElementById('fruits').value);
});

prevButton.addEventListener('click', () => {
  if (page > 1) {
    page--;
    updateCarsVisibility(document.getElementById('fruits').value);
  }
});