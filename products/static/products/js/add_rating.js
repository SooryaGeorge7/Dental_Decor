
var form = document.querySelector('.reviewform');
console.log(form);



var handleRatings = (choice, criteria) => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);
    

    console.log(stars)


    stars.forEach(star => star.classList.remove('checked'));

    var i;
    switch (choice) {
        case `${criteria}-first`:
            for (i = 0; i < 1; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-second`:
            for (i = 0; i < 2; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-third`:
            for (i = 0; i < 3; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-fourth`:
            for (i = 0; i < 4; i++) {
                stars[i].classList.add('checked');
            }
            break;
        case `${criteria}-fifth`:
            for (i = 0; i < 5; i++) {
                stars[i].classList.add('checked');
            }
            break;
    }

    var val_num = getNumValue(choice);
    form[criteria].value = val_num;

};


var getNumValue = (stringValue) => {
    let numValue;
    if (stringValue.endsWith('-first') ) {
        numValue = 1;
    } else if (stringValue.endsWith('-second') ) {
        numValue = 2;
    } else if (stringValue.endsWith('-third') ){
        numValue = 3;
    } else if (stringValue.endsWith('-fourth') ) {
        numValue = 4;
    } else if (stringValue.endsWith('-fifth') ) {
        numValue = 5;
    } else {
        numValue = 0;
    }
    return numValue;
};

var criterias = ['product_rating'];
console.log(criterias)

criterias.forEach(criteria => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);
    console.log(stars)

    stars.forEach(star => {
        star.addEventListener('click', (event) => {
            handleRatings(event.target.id, criteria);

        });
    });
});

var updateStarRatings = (criteria) => {
    var stars = document.querySelectorAll(`.${criteria} .btn i`);
    console.log(stars)
    console.log(criteria)
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
console.log(criterias);

