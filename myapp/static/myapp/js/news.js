$(document).ready(function() {
    $(".news_element h3").click(function() {
      $(this).parent().find("p").show("slow");
    });
  });
  