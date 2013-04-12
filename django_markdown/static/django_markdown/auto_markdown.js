$("textarea[data-markdown-settings]").each(function(i,elt){
  settings = $.extend( mySettings, $.parseJSON($(this).attr("data-markdown-settings")));
  
  markitup = $(this).markItUp(settings);
  /*
  modal = $(this).parents("#modal");
  if (modal.length == 1)
  {
    width = $(this).parents(".controls").width();
    acti = width;
    $(this).parentsUntil($(this).parents(".controls")).each(function(){
      console.debug($(this));
      console.debug($(this).parent().children());
      $(this).parent().children().css("width",acti);
      acti = acti - 10; 
    });
    console.debug($(this).parent().children());
    $(this).parent().children().css("width", width - 55);
  } 
  */
  $(this).removeAttr("data-markdown-settings");
  
  
});
