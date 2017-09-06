
var interval, b = 0;

var start;

var botComand = {
  part: '',
  grades: 0
}

var gamepadIndex = 0;

var gamepadInfo = document.getElementById("gamepadPrompt");

gamepadInfo.innerHTML = "searching gamepad";

/*$(window).keydown(function(e) {
  console.log(e.keyCode);
});

button.addEventListener('pointerup', function(event) {
    navigator.bluetooth.requestDevice({
    filters: [{
      services: ['heart_rate']
    }]
  })
  .then(function(device){ console.log(device.name); return device.gatt.connect();})
  .then(function(server){ server.getPrimaryService('heart_rate');})
  .then(function(service){ service.getCharacteristic('heart_rate_measurement');})
  .then(function(characteristic){characteristic.startNotifications();})
  .then(function(characteristic){
    characteristic.addEventListener('characteristicvaluechanged',
                                    handleCharacteristicValueChanged);
    console.log('Notifications have been started.');
  })
  .catch(function(error) { console.log('error: '+error); });
});*/

window.addEventListener("gamepadconnected", function(e) {
  var gp = navigator.getGamepads()[e.gamepad.index];
  //console.log("Gamepad connected at index " + gp.index + ": " + gp.id + ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
  gameLoop();
});

window.addEventListener("gamepaddisconnected", function(e) {
  console.log("Waiting for gamepad.");
  cancelRequestAnimationFrame(start);
});

if (!('ongamepadconnected' in window)) {
  // No gamepad events available, poll instead.
  gamepadInfo.innerHTML = "no gamepad";
  console.log("no device");
  interval = setInterval(pollGamepads, 500);
}

function pollGamepads() {
	var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads : []);

	for (var i = 0; i < gamepads.length; i++) {

	    var gp = gamepads[i];

      /*gamepadInfo.innerHTML = "Gamepad pollGamepads connected at index " + gp.index + ": " + gp.id +
            ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes."; 

      gamepadIndex = gp.index;

      console.log("Gamepad inside connected at index " + gp.index + ": " + gp.id +
      ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
      gameLoop();
      clearInterval(interval);*/
	    if (gp) {
	    	if( gamepads[i].id.substring(0, 3) != "Unk"){
	    		  gamepadIndex = gp.index;
		      	console.log("Gamepad inside connected at index " + gp.index + ": " + gp.id +  ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
            gamepadInfo.innerHTML =  "Gamepad inside connected at index " + gp.index + ": " + gp.id + ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes."
		      	//gameLoop();
		      	clearInterval(interval);
	    	}
	    }
  	}
}

function buttonPressed(b) {
  if (typeof(b) == "object") {
    return b.pressed;
  }
  return b == 1.0;
}

function gameLoop() {

  var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads : []);

  if (!gamepads) {
    return;
  }
  var gp = gamepads[gamepadIndex];
  if (buttonPressed(gp.buttons[0])) {
    console.log("button 1 pressed! " + botComand.part + " - " + botComand.grades);
    botComand.part = "beebot/shoulder_right";
    if(botComand.grades < 180) botComand.grades += 1;
    gamepadInfo.innerHTML = "button 1 pressed! " + botComand.part + " - " + botComand.grades;
    //publish("beebot/shoulder_right", "+10");
  } 
  else if (buttonPressed(gp.buttons[2])) {
    console.log("button 3 pressed! " + botComand.part + " - " + botComand.grades);
    botComand.part = "beebot/shoulder_right";
    if(botComand.grades > -180) botComand.grades -= 1;
    gamepadInfo.innerHTML = "button 2 pressed! " + botComand.part + " - " + botComand.grades;
    //publish("beebot/shoulder_right", "+10");
  }
  else if (buttonPressed(gp.buttons[1])) {
    console.log("button 2 pressed! " + botComand.part + " - " + botComand.grades);
    botComand.part = "beebot/shoulder_left";
    if(botComand.grades > -180) botComand.grades -= 1;
    gamepadInfo.innerHTML = "button 3 pressed! " + botComand.part + " - " + botComand.grades;
    //publish("beebot/shoulder_left", "-10");
  } 

  else if (buttonPressed(gp.buttons[3])) {
    console.log("button 4 pressed! " + botComand.part + " - " + botComand.grades);
    botComand.part = "beebot/shoulder_left";
    if(botComand.grades < 180) botComand.grades += 1;
    gamepadInfo.innerHTML = "button 4 pressed! " + botComand.part + " - " + botComand.grades;
    //publish("beebot/shoulder_left", "+10");
  }
  else {
    gamepadInfo.innerHTML = "no buttons pressed " + botComand.part + " - " + botComand.grades; 
    console.log("values: " + botComand.part + " - " + botComand.grades);
    botComand.part = '';
    botComand.grades = 0;
  }
  start = requestAnimationFrame(gameLoop);
}

