document.getElementById("addIngredientBtn").addEventListener("click", function() {
  addIngredient();
});

function addIngredient() {
  //Gets input value
  var ingredient = document.getElementById("ingredientInput").value;
  
  //Creates a new item list
  var listItem = document.createElement("li");
  listItem.className = "list-group-item";
  listItem.appendChild(document.createTextNode(ingredient));
  
  //Adds the new items to the ingredients list
  document.getElementById("ingredientList").appendChild(listItem);
  
  //Clears input field
  document.getElementById("ingredientInput").value = "";
}
