
  window.onload = function() {
		console.log("load");
		var stream = document.getElementById('stream');
		var canvas = document.getElementById('canvas');
		main();
	}

// document.querySelector('#video-stream').classList.remove("CLASS_NAME");
	window.plot = function(x, y, w, h) {
		var rect = document.createElement('div');
		document.querySelector('#video-stream').appendChild(rect);
		rect.classList.add('rect');
		rect.style.width = w + 'px';
		rect.style.height = h + 'px';
		rect.style.left = (stream.offsetLeft + x) + 'px';
		rect.style.top = (stream.offsetTop + y) + 'px';
	};


	function main() {
		console.log("main");
		canvas.width = stream.width;
		canvas.height = stream.height;

		tracker = new tracking.ObjectTracker(['face']);
		// tracker = new tracking.ObjectTracker(['face', 'eye', 'mouth']);
		tracker.setStepSize(1.7);

		tracker.on('track', function(event) {
			//Remove old rects
			document.querySelectorAll('.rect').forEach(
				function(node){
					node.parentNode.removeChild(node);
			});
			//Print new rects
			event.data.forEach(function(rect) {
				window.plot(rect.x, rect.y, rect.width, rect.height);
			});
		});
		// loop
		var timer = setInterval(loop, 500);
	}
	function loop() {
		//see: https://stackoverflow.com/questions/19346775/rendering-mjpeg-stream-in-html5
		var ctx = canvas.getContext("2d");
		ctx.drawImage(stream, 0, 0);
		tracking.track('#canvas', tracker);
	}