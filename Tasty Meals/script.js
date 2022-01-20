  var seconds=0;
  function displayseconds()
  {
      seconds +=1;
      document.getElementById("mani2012").innerText="This page will be redirected In "+seconds+" seconds...";
  }
  setInterval(displayseconds,2000);

  function redirectpage()
  {
      window.location="recipes.html";
  }
  setTimeout('redirectpage()',7000);


