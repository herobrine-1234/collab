$(function () {
    var syncClient;
    var syncStream;
    var message = document.getElementById('message');
    var text_area = document.getElementById('text_area');
    var select_element = document.getElementById('select')
    var background_color;


    $.getJSON('/token', function(tokenResponse) {
        syncClient = new Twilio.Sync.Client(tokenResponse.token, { logLevel: 'info' });

        // create the stream object
        syncClient.stream('messageData').then(function(stream) {
            syncStream = stream;
            // listen update and sync drawing data
            syncStream.on('messagePublished', function(event) {
                console.log('syncStream:',event.message.value);
                syncDrawingData(event.message.value);


            });
        });
    });

function syncDrawingData(data){
    console.log(data);
}

function messageSync(){
   data=document.getElementById("text_area").value
   setTimeout(function(){
    SettingSyncData()
   },1700);
}

function SettingSyncData(){
    syncStream.publishMessage(
    {text_area_value: data}
        );
    
    }
    text_area.addEventListener("keyup", messageSync);



});
