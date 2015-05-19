% rebase('layout.tpl', title='Credit Card Validator Service')


<h1>Credit Card Validation Service </h1>
<p>This is a demonstration of service composition using BPEL</p>


<form method="post" action="result">
<label for="cc_number">Credit Card Number:</label>
<input type="text" name="cc_number" placeholder="Enter cc number">
<input type="submit">
<button id="rest_btn">REST call </button><span id="loader" class="hidden"><img src="/static/loader.gif"></span>
</form>
<p>Please <b>NEVER</b> submit a real credit card number to such a service.</p>


<div id="rest_response"></div>

<br/><br/><br/><br/>
<button id="cc_toggle">Toggle sample credit card numbers</button>
<pre class="hidden" id="cc_list">
Visa
4556394058714517
4024007153623862
4556916306788131
4539813411571027
4929579555719833

Mastercard
5133500428180457
5160974949800586
5134365511449055
5325762900224314
5297424400804830

Discover
6011831866388475
6011428578181361
6011182261842009
6011055401753551
6011489972733017

American Express
342108421246925
349108457274620
379960009989342
347911944560218
349880111725797
</pre>

<script>
$("#cc_toggle").click(function(e){
    $("#cc_list").toggle();
});

$("#rest_btn").click(function(e){
    $('#loader').show()
    var nb = $("input[name=cc_number]").val();
    //console.log(nb);
    $.get("/validator/" + nb, function(res){
        console.log(res.type);
        $('#rest_response').append("<p>" + nb + " is "  + res.type +"</p>" );
    }).always(function(){
        $('#loader').hide()
    })
    return false;
});


</script>