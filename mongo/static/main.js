let nameA = true;
let dateA = true;
let servA = true;
let cookA = true;
let ingA = true;

function generateHTMLFromJSON() {
  var contentContainer = document.getElementById('content');
 // contentContainer = "";
  var it = 0;
  jsonArray.forEach(function(item) {

  var itemDiv = document.createElement('div');
  itemDiv.className = 'item';


  itemDiv.innerHTML = `
  <div class="row">
  <div class="col-md"><a href="#">${item.name}</a></div>
  <div class="col-md">${item.ing} </div>
  <div class="col-md">${item.servings}</div>
  <div class="col-md">${item.cook} </div>
  <div class="col-md">${item.date}</div>
  <div class="col-md">


  <p>
<a class="btn btn-primary" data-toggle="collapse" href="#${it.toString()}" role="button" aria-expanded="false" aria-controls="${it.toString()}">
Tags
</a>
</p>
<div class="collapse" id="${it.toString()}">
<div class="card card-body">
${item.tags} 
</div>
</div>



</div>
</div>
`;
it += 1;


contentContainer.appendChild(itemDiv);
});
}

 jsonArray = [];
window.onload = function() {
  //generateHTMLFromJSON();
  getData();
  generateHTMLFromJSON();
};
function getData(){
  const url ='http://127.0.0.1:5000/getData'
    fetch(url)
    .then(response =>response.json())
    .then(json=>{
        //console.log(json.Jack);
        console.log(json);
        //alert(json[0].name);
        for(var i = 0; i < json.length; ++i){
        /*jsonArray[i].name = json[i].name;
        jsonArray[i].ing = json[i].numIngredients;
        jsonArray[i].cook = json[i].cookTime;
        jsonArray[i].servings = json[i].numServings;
        jsonArray[i].date = json[i].date;
        */
        var item = {"name": json[i].name, "ing": json[i].numIngredients, "cook": json[i].cookTime, "servings": json[i].numServings, "date": json[i].date}; 
        jsonArray.push(item);
        }
        /*
        for(let i = 0; i < json.length; i++){
            let obj = json[i];
            alert(obj.name);
        }*/
        })
//  alert(jsonArray);
  generateHTMLFromJSON();
}
function sortIngredients(){
  var container = document.getElementById('content');
  container.innerHTML = '';
  jsonArray.sort(function(a, b) {
      if(ingA == true){
      return a.ing - b.ing;
      }else{
      return b.ing - a.ing;
      }
      });
  generateHTMLFromJSON(); 
}
function sortCook(){
  var container = document.getElementById('content');
  container.innerHTML = '';
  jsonArray.sort(function(a, b) {
      if(cookA == true){
      return a.cook - b.cook;
      }else{
      return b.cook - a.cook;
      }
      });
  generateHTMLFromJSON();  
}
function sortName(){
  var container = document.getElementById('content');
  container.innerHTML = '';
  if (nameA == false) {
    jsonArray.sort(function(a, b) {
        if (a.name < b.name) {
        return -1;
        }
        if (a.name > b.name) {
        return 1;
        }
        return 0;
        });
  } else {
    jsonArray.sort(function(a, b) {
        if (a.name > b.name) {
        return -1;
        }
        if (a.name < b.name) {
        return 1;
        }
        return 0;
        });
  }
  generateHTMLFromJSON();

}
function sortServings(){
  var container = document.getElementById('content');
  container.innerHTML = '';
  jsonArray.sort(function(a, b) {
      if(servA == true){
      return a.servings - b.servings;
      }else{
      return b.servings - a.servings;
      }
      });
  generateHTMLFromJSON(); 
}
function sortDate(){
  var container = document.getElementById('content');
  container.innerHTML = '';
  //jsonArray.sort(function(a, b) {
  if (dateA == true) {
    jsonArray.sort((a,b) => a.date - b.date);
  } else {
    jsonArray.sort((a,b) => b.date - a.date);
  }
  generateHTMLFromJSON(); 
}



function onClickName() {
  var buttons = document.querySelectorAll("[tag='name']");

  buttons.forEach(function(button) {
      if (nameA) {
      button.textContent = "Name Z->A";
      } else {
      button.textContent = "Name A->Z";
      }
      });

  sortName(); 
  nameA = !nameA;
}
function onClickIng() {
  var buttons = document.querySelectorAll("[tag='numIng']");


  buttons.forEach(function(button) {
      if (ingA) {
      button.textContent = "# of Ingredients L->G";
      } else {
      button.textContent = "# of Ingredients G->L";
      }
      });
  sortIngredients();
  // Toggle the state
  ingA = !ingA;
}
function onClickDate() {
  var buttons = document.querySelectorAll("[tag='date']");

  buttons.forEach(function(button) {
      if (dateA) {
      button.textContent = "Date L->G";
      } else {
      button.textContent = "Date G->L";
      }
      });
  sortDate();


  dateA = !dateA;
}
function onClickServ() {
  var buttons = document.querySelectorAll("[tag='serv']");

  buttons.forEach(function(button) {
      if (servA) {
      button.textContent = "Servings L->G";
      } else {
      button.textContent = "Servings G->L";
      }
      });
  sortServings();


  servA = !servA;
}
function onClickCook() {
  var buttons = document.querySelectorAll("[tag='cook']");

  buttons.forEach(function(button) {
      if (cookA) {
      button.textContent = "Cook Time L->G";
      } else {
      button.textContent = "Cook Time G->L";
      }
      });
  sortCook();

  cookA = !cookA;
}
