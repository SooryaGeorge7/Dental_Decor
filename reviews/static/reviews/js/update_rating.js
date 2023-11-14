var form = document.querySelector('.reviewform');
var criterias = ['product_rating'];
console.log(form)

var myElement = document.getElementById('myElement');

// Add the 'myClass' class to the element
myElement.classList.add('myClass');

var updateStarRatings = (criteria) => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);
    var value = form[criteria].value;
    console.log(value)
    stars.forEach((star, index) => {
      if (index < value) {
        star.classList.add('checked');
      } else {
        star.classList.remove('checked');
      }
    });
  };
  
  
  criterias.forEach(criteria => {
    updateStarRatings(criteria);
  });