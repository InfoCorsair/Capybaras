//Brendan Schweichler
//Export/Import json functions

function showSelection() {
  var selectBox = document.getElementById("recipeSelection");
  var selectedValue = selectBox.options[selectBox.selectedIndex].value;
  document.getElementById("recipeSelect").innerHTML = selectedValue;
}