/***********************************
	INGREDIENTS.JS

 Ingredients.js is the JavaScript file
 responisble for adding additional ingredients
 to a recipe.

***********************************/
//document.getElementById("addIngredientBtn").addEventListener("click", function() {
 // addIngredient();
//});

function addIngredient() {
  //Gets input value
  var ingredient = document.getElementById("ingredientInput").value;
  
  //Creates a new item list
  var listItem = document.createElement("li");
  listItem.className = "list-group-item";
  listItem.appendChild(document.createTextNode(ingredient));
  
  
  var deleteButton = document.createElement("button");
  deleteButton.className = "btn btn-primary btn-sm float-right";
  deleteButton.innerHTML = "Remove Ingredient";
  
  
  deleteButton.onclick=function() 
  {
    listItem.remove();
  }
  
  
  //Adds the new items to the ingredients list
  listItem.appendChild(deleteButton);
  document.getElementById("ingredientList").appendChild(listItem);


  //Clears input field
  document.getElementById("ingredientInput").value = "";
}


function toggleButton(elem) {
  var x = document.getElementById(elem);
  if(x.style.display == "none")
    x.style.display ="block";
  else
    x.style.display ="none";
}

submitInfo = function(){
  document.forms["form1"].submit();
}


function removeIngredients(button){
  document.getElementById("listItem"+button+"").outerHTML="";

}
