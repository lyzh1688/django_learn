/**
 * Created by Yuezhi.Liu on 2016/4/1.
 */
function OnSearch()
{
    ///record/detail/3/201604
    var month = $('#month').val()
    var year = $('#year').val()
    date = year + month
    $(window.location).attr('href', '/tax/' + date + '/' );
}