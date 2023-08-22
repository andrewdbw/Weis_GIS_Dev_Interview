
/**
 * Take a array of dictionaries containing name and age and log
 * to console an array of names whose age is less than 50
 * 
 * @param {Array} peopleArray [Array of dictionaries with format {'name' : name, 'age' : age}] 
 *
 */
function getPeopleUnder50(peopleArray) {
    
    const returnArray = [];
    
    for (p in peopleArray) {
        
        let age = peopleArray[p].age
        
        if (age < 50 && age != null) {
            returnArray.push(peopleArray[p].name);
        }
    }
    
    console.log(returnArray);
    
}

/**
 * Logs all div ids to consold
 */
function getDivIds() {
    
    var divs = document.getElementsByTagName("div");

    for (var i = 0; i < divs.length; i++) {
        console.log(divs[i].id)
    }

}




