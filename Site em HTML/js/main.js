var slider = new Slider({
	background: ".js-slider-background",
	items: ".js-slider-items",
	link: ".js-slider-link",
	nav: ".js-slider-nav",
	slider: ".js-slider"
});

var circleProgress = new progressBar({
	type: "circle",
    targetClass: "round-progress",
    value: 0,
    duration: 1000,
    completeDuration: 0
});

circleProgress.setCircleProgress(75);