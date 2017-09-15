
var interval, b = 0;

var start;

var botComand = {
  part: '',
  grades: 0,
  action: '', 
  direction: '',
  incremental: 1,
  lStatus: false,
  rStatus: false,
  buttonTrigger: false
}

var axisCleaned = true;

var gamepadIndex = 0;

var gamepadInfo = document.getElementById("gamepadPrompt");

gamepadInfo.innerHTML = "searching gamepad";

$(window).keydown(function(e) {
  console.log(e.keyCode);
  gamepadInfo.innerHTML = e.keyCode;
});

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
      if (gp) {
        if( gamepads[i].id.substring(0, 3) != "Unk"){
            gamepadIndex = gp.index;
            console.log("Gamepad inside connected at index " + gp.index + ": " + gp.id +  ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes.");
            console.log(gp.axes);
            gamepadInfo.innerHTML =  "Gamepad inside connected at index " + gp.index + ": " + gp.id + ". It has " + gp.buttons.length + " buttons and " + gp.axes.length + " axes."
            gameLoop();
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

function cleanGamePad(){
  document.getElementById("headButton1").style.display = "none";
  document.getElementById("rightArmButton1").style.display = "none";
  document.getElementById("platformButton1").style.display = "none";
  document.getElementById("leftArmButton1").style.display = "none";
}
function cleanAxes(){
  document.getElementById("upAxis1").style.display = "none";
  document.getElementById("downAxis1").style.display = "none";
  document.getElementById("leftAxis1").style.display = "none";
  document.getElementById("rightAxis1").style.display = "none";
  axisCleaned = true;
}

function gameLoop() {

  var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads : []);
  
  if (!gamepads) {
    return;
  }
  var gp = gamepads[gamepadIndex];

  gamepadInfo.innerHTML = "get into gameLoop " + gp.buttons[0].pressed;  
  
  if ( gp.buttons[0].pressed ) {
    botComand.part = "head";
    gamepadInfo.innerHTML = "button 1 pressed! " + botComand.part + " - " + botComand.grades;
    cleanGamePad();
    document.getElementById("headButton1").style.display = "block";
    //publish("beebot/shoulder_right", "+10");
  } 
  else if (gp.buttons[1].pressed) {
    botComand.part = "shoulder_right";
    gamepadInfo.innerHTML = "button 2 pressed! " + botComand.part + " - " + botComand.grades;
    cleanGamePad();
    document.getElementById("rightArmButton1").style.display = "block";
    //publish("beebot/shoulder_right", "+10");
  }
  else if (gp.buttons[2].pressed) {
    botComand.part = "platform";
    gamepadInfo.innerHTML = "button 3 pressed! " + botComand.part + " - " + botComand.grades;
    cleanGamePad();
    document.getElementById("platformButton1").style.display = "block";
    //publish("beebot/shoulder_left", "-10");
  } 
  else if (gp.buttons[3].pressed) {
    botComand.part = "shoulder_left";
    gamepadInfo.innerHTML = "button 4 pressed! " + botComand.part + " - " + botComand.grades;
    cleanGamePad();
    document.getElementById("leftArmButton1").style.display = "block";
    //publish("beebot/shoulder_left", "+10");
  } 
  else if (gp.buttons[4].pressed) {
    gamepadInfo.innerHTML = "button L pressed! ";
    if(botComand.buttonTrigger == false){
      botComand.buttonTrigger = true;
      console.log("button L", botComand.buttonTrigger );
      if(botComand.lStatus == false){
        document.getElementById("LButton1").style.display = "block";
        botComand.lStatus = true;
        publish("beebot/webcam/switch", "0");
      }
      else{
        document.getElementById("LButton1").style.display = "none";
        botComand.lStatus = false;
        publish("beebot/webcam/switch", "0"); 
      }
    }
    //publish("beebot/shoulder_left", "+10");
  } 
  else if (gp.buttons[5].pressed) {
    gamepadInfo.innerHTML = "button R pressed! ";
    if(botComand.buttonTrigger == false){
      botComand.buttonTrigger = true;
      console.log("button R", botComand.buttonTrigger );
      if(botComand.rStatus == false){
        document.getElementById("RButton1").style.display = "block";
        publish("beebot/laser/fire", "0");
        botComand.rStatus = true;
      }
      else{
        document.getElementById("RButton1").style.display = "none";
        publish("beebot/laser/fire", "0"); 
        botComand.rStatus = false; 
      }
    }
    //publish("beebot/shoulder_left", "+10");
  } 
  else if (gp.axes[0] == -1){
    document.getElementById("leftAxis1").style.display = "block";
    axisCleaned = false;
    if( botComand.part ==  'head' ){ botComand.action = "beebot/head_pan"; botComand.incremental = 1; }
    if( botComand.part ==  'platform' ){ botComand.action = "beebot/platform/turn_left"; botComand.incremental = 0.02; }
    if( botComand.part ==  'shoulder_left' ){ botComand.action = "beebot/elbow_left"; botComand.incremental = 1; }
    if( botComand.part ==  'shoulder_right' ){ botComand.action = "beebot/elbow_right"; botComand.incremental = 1; }
    if( botComand.grades < 180 ) botComand.grades += botComand.incremental;
    if( botComand.part ==  'platform' || botComand.part ==  'shoulder_right' ) botComand.direction = "+";
    else  botComand.direction = "-";
    console.log("axe 1 pressed left " + botComand.action + " - " + botComand.grades);
  }
  else if (gp.axes[0] == 1){
    document.getElementById("rightAxis1").style.display = "block";
    axisCleaned = false;
    if( botComand.part ==  'head' ){ botComand.action = "beebot/head_pan"; botComand.incremental = 1; }
    if( botComand.part ==  'platform' ){ botComand.action = "beebot/platform/turn_right"; botComand.incremental = 0.02; } 
    if( botComand.part ==  'shoulder_left' ){ botComand.action = "beebot/elbow_left"; botComand.incremental = 1; } 
    if( botComand.part ==  'shoulder_right' ){ botComand.action = "beebot/elbow_right"; botComand.incremental = 1; }
    if(botComand.grades < 180) botComand.grades += botComand.incremental;
    if( botComand.part ==  'shoulder_right' ) botComand.direction = "-";
    else botComand.direction = "+";
    console.log("axe 1 pressed right " + botComand.action + " - " + botComand.grades);  
  }
  else if (gp.axes[1] == -1){
    document.getElementById("upAxis1").style.display = "block";
    axisCleaned = false;
    if( botComand.part ==  'head' ){ botComand.action = "beebot/head_tilt"; botComand.incremental = 1; }
    if( botComand.part ==  'platform' ){ botComand.action = "beebot/platform/forward"; botComand.incremental = 0.02; } 
    if( botComand.part ==  'shoulder_left' ){ botComand.action = "beebot/shoulder_left"; botComand.incremental = 1; }  
    if( botComand.part ==  'shoulder_right' ){ botComand.action = "beebot/shoulder_right"; botComand.incremental = 1; }
    if(botComand.grades < 180) botComand.grades += botComand.incremental;
    if( botComand.part ==  'shoulder_right' ) botComand.direction = "-";
    else botComand.direction = "+";
    console.log("axe 1 pressed up " + botComand.action + " - " + botComand.grades);
  }
  else if (gp.axes[1] == 1){
    document.getElementById("downAxis1").style.display = "block";
    axisCleaned = false;
    if( botComand.part ==  'head' ){ botComand.action = "beebot/head_tilt"; botComand.incremental = 1; }
    if( botComand.part ==  'platform' ){ botComand.action = "beebot/platform/backward"; botComand.incremental = 0.02; }
    if( botComand.part ==  'shoulder_left' ){ botComand.action = "beebot/shoulder_left"; botComand.incremental = 1; }
    if( botComand.part ==  'shoulder_right' ){ botComand.action = "beebot/shoulder_right"; botComand.incremental = 1; }
    if( botComand.grades < 180 ) botComand.grades += botComand.incremental;
    if( botComand.part ==  'platform' || botComand.part ==  'shoulder_right') botComand.direction = "+";
    else  botComand.direction = "-";
    console.log("axe 1 pressed down " + botComand.action + " - " + botComand.grades);
  }
  else {    
    //gamepadInfo.innerHTML = "no buttons pressed " + gameLoopCounter; 
    //publish(botComand.action, botComand.direction + botComand.grades.toString());
    if(!axisCleaned) cleanAxes();
    if( botComand.grades != 0 && botComand.action != '' ) {
      publish(botComand.action, botComand.direction + (10 * botComand.incremental).toString());
     } 
    if(!axisCleaned) cleanAxes();
    if( botComand.grades != 0 ) console.log("values: " + botComand.action + " - " + botComand.direction + (10 * botComand.incremental).toString());
    botComand.grades = 0;
    botComand.buttonTrigger = false;
  }
  start = requestAnimationFrame(gameLoop);
}
