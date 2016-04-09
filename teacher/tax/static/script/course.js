/**
 * Created by Yuezhi.Liu on 2016/4/1.
 */
$(document).ready(function() {
    //toggle `popup` / `inline` mode
    $.fn.editable.defaults.mode = 'inline';
    $.fn.editable.defaults.ajaxOptions = {type: "GET"};
    //make username editable
    $("a[name='fee']").editable(
        {type:'text',
         pk: 1,
         url: '/course/edit/fee/',
         title: 'Enter Fee'}
    );


});

function OnSelectTeacher(id,name)
{
    $('#teachername').val(name);
    $('#teacherid').val(id);
}

function OnDeleteHandle(course_id,teacher_id)
{
    var aj = $.ajax( {
        url:'/class/del/',
        data:{
            course_id:course_id,
            teacher_id :teacher_id
        },
         type:'get',
         dataType:'json',
         success:function(data) {
             var redirectUrl = '/course/detail/' + course_id + '/';
             $(window.location).attr('href', redirectUrl);
          },
          error : function() {
               // view("异常！");
               alert("异常！");
          }
     });
}
