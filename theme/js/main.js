"use strict";

document.addEventListener("DOMContentLoaded", function(event) {
// Pick a random buzzword to kick some asses
	var buzzwords = [
		"hydroponics",
		"IoT",
		"tech",
		"HiFi",
		"houseplants",
		"OSS",
		"&#127828;",
		"&#128021;",
		"&#127793;"
	];

	var container = document.getElementById("buzzword")
	// element content must be cleaned for typed.js
	container.innerHTML = "";

	new Typed("#buzzword", {
		strings: [buzzwords[Math.floor(Math.random() * buzzwords.length)]],
		typeSpeed: 30,
		loop: false,
		showCursor: true,
		onComplete: function() {
			window.setTimeout(function(){document.querySelectorAll(".typed-cursor")[0].style.display = "none"}, 333);
		}
	});
});
