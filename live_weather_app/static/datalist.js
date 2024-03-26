var findCity = document.querySelector('#cityInput');
var cityresults = document.querySelector('#resultList');
var allplaces = document.querySelector('#allPlaces').content;
findCity.addEventListener('keyup', function handler(event) {
    while (cityresults.children.length) cityresults.removeChild(cityresults.firstChild);
    var inputVal = new RegExp(findCity.value.trim(), 'i');
    var set = Array.prototype.reduce.call(allplaces.cloneNode(true).children, function findCityFilter(frag, item, i) {
        if (inputVal.test(item.textContent) && frag.children.length < 6) frag.appendChild(item);
        return frag;
    }, document.createDocumentFragment());
    cityresults.appendChild(set);
});