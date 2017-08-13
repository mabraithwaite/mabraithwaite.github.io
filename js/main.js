function main() {
  $('.my-button').on('click', function () {
    var selectedSort = $('.my-select').find(":selected").text();

    switch (selectedSort) {
      case "Alphabetic [A-Z]":
        $.getJSON("json/dogs.json", function(json) {
          json.dogs.sort(function compare(a, b) {
            if (a.name < b.name)
              return -1;
            if (a.name > b.name)
              return 1;
            return 0;
          })
          $('.container').html(buildHTML(json.dogs))
        })
        break;
      case "Alphabetic [Z-A]":
        $.getJSON("json/dogs.json", function(json) {
          json.dogs.sort(function compare(a, b) {
            if (a.name < b.name)
              return 1;
            if (a.name > b.name)
              return -1;
            return 0;
          })
          $('.container').html(buildHTML(json.dogs))
        })
        break;
      case "Age [Youngest-Oldest]":
        $.getJSON("json/dogs.json", function(json) {
          json.dogs.sort(function compare(a, b) {
            return 12 * (a.age.year - b.age.year) + (a.age.month - b.age.month);
          })
          $('.container').html(buildHTML(json.dogs))
        })
        break;
      case "Age [Oldest-Youngest]":
        $.getJSON("json/dogs.json", function(json) {
          json.dogs.sort(function compare(a, b) {
            return 12 * (b.age.year - a.age.year) + (b.age.month - a.age.month);
          })
          $('.container').html(buildHTML(json.dogs))
        })
        break;
      default:

    }
  });

  $.getJSON("json/dogs.json", function(json) {
    $('.container').html(buildHTML(json.dogs))
  })
}

function buildHTML(dogs) {
  var html = ""
  for (var i = 0; i < dogs.length; i++) {
    html += buildDogDiv(dogs[i])
  }

  return html
}

function buildDogDiv(dog) {
  var html = ""
  html += "<div class=\"dog\">"
  html +=        "<img src=\"" + dog.image + "\" class=\"dog-pic inline\">"
  html +=        "<h3>" + dog.name + "</h3>"
  html +=        "<div class=\"good-with\">"
  html +=          "<table class=\"good-with\" cellpadding=\'0\' cellspacing=\'5\'>"
  html +=            "<tr>"
  html +=              "<th colspan=\'3\'>Good With</th>"
  html +=            "</tr>"
  html +=            "<tr>"
  html +=              "<th>Dogs</th>"
  html +=              "<th>Cats</th>"
  html +=              "<th>Children</th>"
  html +=            "</tr>"
  html +=            "<tr>"
  html +=              "<td>" + dog.goodWithDogs + "</td>"
  html +=              "<td>" + dog.goodWithCats + "</td>"
  html +=              "<td>" + dog.goodWithChildren + "</td>"
  html +=            "</tr>"
  html +=          "</table>"
  html +=        "</div>"
  html +=        "<p><b>Breed:</b> " + dog.breed + "</p>"
  html +=        "<p><b>Gender:</b> " + dog.gender + "</p>"
  if (dog.age.year === 0 && dog.age.month === 0) {
    html +=        "<p><b>Age:</b> " + dog.age.ageStr + "</p>"
  } else {
    html +=        "<p><b>Age:</b> "
    if (dog.age.year > 0) {
      html += dog.age.year + ((dog.age.year > 1) ? " years" : " year")
    }
    if (dog.age.month > 0) {
      html += ((dog.age.year > 0) ? ", " : "") + dog.age.month + ((dog.age.month > 1) ? " months" : " month")
    }

    html += "</p>"
  }
  html +=        "<p><b>Housetrained:</b> " + dog.housetrained + "</p>"
  if (dog.bio !== ""){
    html +=        "<p><b>Bio:</b> " + dog.bio + " </p>"
  }
  html +=    "</div>"
  return html
}

$(document).ready(main)
