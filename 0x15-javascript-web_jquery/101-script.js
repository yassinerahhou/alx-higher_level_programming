$(function () {
  //When the user clicks on DIV#add_item: a new element is added to the list
  $("DIV#add_item").click(function () {
    $("UL.my_list").append("<li>Item</li>");
  });
  $("DIV#remove_item").click(function () {
    // the last element is removed from the list
    $("UL.my_list li").last().remove();
  });
  $("DIV#clear_list").click(function () {
    //all elements of the list are removed
    $("UL.my_list").empty();
  });
});

