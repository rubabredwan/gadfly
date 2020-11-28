$(document).ready(function(){
  $(".title").hide();
  $(".card").click(function(e){
    console.log('ok');
    $(this).children('.title').show();
  })
})
