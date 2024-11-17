import Building from './Building.js';

export default class ResidentialBuilding extends Building {
constructor(sqft, numOfApartments) {
super(sqft);
this.numOfApartments = numOfApartments;
}

get numOfApartments() {
return this._numOfApartments;
}

set numOfApartments(value) {
if (typeof value !== 'number') {
throw new TypeError('numOfApartments must be a number');
}
this._numOfApartments = value;
}

evacuationWarningMessage() {
return 'Evacuate the Residential Building immediately!';
}
}
