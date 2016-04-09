/**
 * Created by Yuezhi.Liu on 2016/4/1.
 */
function OnClickNavHandle(id)
{
    $('#'+id).attr("class", "active");
    //main-nav
}

function DeleteHandle(teacher_id)
{
    var aj = $.ajax( {
        url:'/teacher/del/',
        data:{
            teacher_id :teacher_id
        },
         type:'get',
         dataType:'json',
         success:function(data) {
             $(window.location).attr('href', '/teacher');
          },
          error : function() {
               // view("异常！");
               alert("异常！");
          }
     });
}