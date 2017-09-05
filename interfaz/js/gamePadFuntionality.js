
var interval, b = 0;

var gamepadIndex = 0;

var gamepadInfo = document.getElementById("gamepadPrompt");

gamepadInfo.innerHTML = "searching gamepad";

window.addEventListener("gamepadconnected", function(e) {
  var gp = navigator.getGamepads()[e.gamepad.index];
  console.log("Gamepad connected at index " + gp.index + ": " + gp.id + ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
  //console.log("Gamepad connected at index " + gp.index + ": " + gp.id + ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
  gameLoop();
});

window.addEventListener("gamepaddisconnected", function(e) {
  console.log("Waiting for gamepad.");
  cancelRequestAnimationFrame(start);
});

if (!('ongamepadconnected' in window)) {
  // No gamepad events available, poll instead.
  gamepadInfo.innerHTML = "founded";
  interval = setInterval(pollGamepads, 500);
}

function pollGamepads() {
	var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads : []);
	for (var i = 0; i < gamepads.length; i++) {

	    var gp = gamepads[i];

      gamepadInfo.innerHTML = "Gamepad inside connected at index " + gp.index + ": " + gp.id +
            ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes."; 

      gamepadIndex = gp.index;

      console.log("Gamepad inside connected at index " + gp.index + ": " + gp.id +
      ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
      gameLoop();
      clearInterval(interval);
	    
	    /*if (gp) {
	    	if( gamepads[i].id.substring(0, 3) != "Unk"){
	    		  gamepadIndex = gp.index;
		      	console.log("Gamepad inside connected at index " + gp.index + ": " + gp.id +
		        ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
		      	gameLoop();
		      	clearInterval(interval);
	    	}
	    }*/
  	}
}

function buttonPressed(b) {
  if (typeof(b) == "object") {
    return b.pressed;
  }
  return b == 1.0;
}

function gameLoop() {

  gamepadInfo.innerHTML = "inside gameLoop"; 

  var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads : []);
  if (!gamepads) {
    return;
  }
  var gp = gamepads[gamepadIndex];
  console.log(gp);
  if (buttonPressed(gp.buttons[0])) {
    console.log("button 1 pressed!");
    gamepadInfo.innerHTML = "button 1 pressed!";
    publish("beebot/shoulder_right", "+10");
  } else if (buttonPressed(gp.buttons[2])) {
    console.log("button 3 pressed!");
    publish("beebot/shoulder_right", "-10");
  }
  if (buttonPressed(gp.buttons[1])) {
    console.log("button 2 pressed!");
    publish("beebot/shoulder_left", "-10");
  } else if (buttonPressed(gp.buttons[3])) {
    console.log("button 4 pressed!");
    publish("beebot/shoulder_left", "+10");
  }
  window.requestAnimationFrame(gameLoop);
}