$(document).ready(function() {

  var newInput = `<div class='row justify-content-center inputdata'>
    <div class='col-lg-4 text-center grcol'>
      <input type='text' class='form-control' placeholder='Test 1'>
    </div>
    <div class='col-lg-4 text-center grcol'>
      <div class='input-group mb-3'>
        <input type='number' name='grades[]' class='form-control' placeholder='100%' min='0' max='100'>
        <div class='input-group-append'>
          <span class='input-group-text' id='basic-addon2'>%</span>
        </div>
      </div>
    </div>
    <div class='col-lg-4 text-center grcol'>
      <input type='number' name='weights[]' class='form-control' placeholder='40' min='0' max='100'>
    </div>
  </div>`

  $("#addField").on('click', function(e) {
    e.preventDefault();
    $(".inputdata").last().after(newInput);
  });

  $("#submit").on('click', function(e) {

    e.preventDefault();
    var dataa = {name: "test"};
    $.ajax({
      type: "POST",
      data: dataa,
      dataType: 'text',
      success: function(data) {
        var test = "{{ date }}";
        console.log("{{ test }}");
        console.log("test");
        console.log('exdee')
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        console.log(errorThrown);
        console.log("test");
      },
    });
  });


});
