/**
 * Created by Yuezhi.Liu on 2016/4/1.
 */
$(document).ready(function() {
    //toggle `popup` / `inline` mode
    $.fn.editable.defaults.mode = 'inline';
    $.fn.editable.defaults.ajaxOptions = {type: "GET"};
    //make username editable
    $("a[name='times']").editable(
        {type:'text',
         pk: 1,
         url: '/record/settimes/',
         title: 'Enter username'}
    );


});

function OnEditRecordDetail(month)
{
    ///record/detail/3/201604
    var course_id = $('#course_id').val()
    var year = $('#year').val()
    $(window.location).attr('href', '/record/detail/' + course_id + '/' + year + month );
}