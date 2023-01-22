console.log('okds');

// This evevt listener will call at the time of single data insertion
document.getElementById("singleSubmitBtn").addEventListener("click", (e) => {
  // getting data HTML form
  let name = document.getElementById("name").value;
  let address = document.getElementById("Address").value;
  let gender = document.getElementById("Gender").value;
  let mobileno = document.getElementById("mobno").value;

  // above single person data will be send to the database through the XMLHTTPRequest
  var xhr = new XMLHttpRequest();
  // setting request headers
  xhr.setRequestHeader("Content-Type", "application/json");

  // whenever the request state is change it reflects in this function
  xhr.onreadystatechange = function () {
    if (this.status != 200) {
      console.log("err -> " + this.responseText);
    } else if (this.status == 200) {
      console.log("res -> " + JSON.stringify(this.responseText));
    }
  };

  // sending form data to server
  xhr.send(
    JSON.stringify({
      name: name,
      gender: gender,
      address: address,
      mobileno: mobileno,
    })
  );
});

// while searching, there is keyUp event listener for search box, it will be called below function
$("#searchInput").keyup((e) => {
  e.preventDefault();

  // getting search parameter
  let q = document.getElementById("searchInput").value;

  // if the search bar is not empty then search 
  // else remove previous search
  if (q != "") {
    $(".dumpFilter").empty();
    $.ajax({
      type: "GET",
      url: `search/?q=${q}`,
      dataType: "json",
      success: (data) => {
        // console.log(data);
        // console.log(data.found);
        data.hits.map((item) => {
          $(".dumpFilter").append(`
            <div class="">
                <p class="text-lime-200 text-sm font-semibold">${item.document.name}</p>
                <div class="flex justify-start py-1">
                    <p class="text-lime-400 mr-4 text-xs ">Gender: <span class="font-bold text-white">${item.document.gender}</span></p>
                    <p class="text-lime-400 mr-4 text-xs">Address: <span class=" text-white">${item.document.address}</span></p>
                    <p class="text-lime-400 mr-4 text-xs">MobNo: <span class=" text-white">${item.document.mobileno}</span></p>
                </div>
            </div>
            <hr class="text-white mx-2 py-2">
          `);
        });
      },
      error: (xhr, status, error) => {
        console.error(error);
      },
    });
  } else {
    $(".dumpFilter").empty();
  }
});


// it's just UI thing
$(".filter").hide((e) => {
  $(".dumpFilter").empty();
});
$("#searchInput").focus((e) => {
  e.preventDefault();
  console.log("d");
  $(".formContainer").hide();
  $(".filter").show();
});

$("#searchInput").focusout((e) => {
  e.preventDefault();
  console.log("df");
  $(".formContainer").show();
  $(".filter").hide();
});
