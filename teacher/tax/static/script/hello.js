function onLoad()
{
    //alert('init');
}

function ClickHandle()
{
    alert('ajax');
    var aj = $.ajax( {
        url:'/test',
        data:{
            name :'Jennifer'
        },
         type:'get',
         cache:false,
         dataType:'json',
         success:function(data) {
             $("p").text(data.name);
          },
          error : function() {
               // view("异常！");
               alert("异常！");
          }
     });
}