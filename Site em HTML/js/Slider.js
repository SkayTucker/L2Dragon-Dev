class Slider {
	constructor(params) {
		this._elements = {
			background: document.querySelector(params.background),
			items: document.querySelector(params.items),
			link: document.querySelector(params.link),
			nav: document.querySelector(params.nav),
			slider: document.querySelector(params.slider),
			dots: null
		};
		this._data = null;
		this._width = null;
		this._next = null;
		this._prev = null;
		this._currentIndex = 0;
		this._init();
	}

	_onClick(direction) {
		this._changeSlide(direction);
	}

	_createElement(type) {
		var element = document.createElement("div");

		element.classList.add(type);

		return element;
	}

	_getDataItems() {
		var data = [];

		for(var i = 0; i < this._elements.items.children.length; i++) {
			var item = this._elements.items.children[i];

			data.push({
				background: item.getAttribute("data-background"),
				link: item.getAttribute("data-link"),
			})
		}

		return data;
	}

	_getWidth() {
		return this._elements.slider.offsetWidth;
	}

	_setItemWidth(width) {
		for(var i = 0; i < this._data.length; i++) {
			var item = this._elements.items.children[i];

			item.style.width = width + "px";
		}
	}

	_createNavItems() {
		var dots = this._createElement("slider__dots");
		var prev = this._createElement("slider__prev");
		var next = this._createElement("slider__next");

		for(var i = 0; i < this._elements.items.children.length; i++) {
			var dot = this._createElement("slider__dot");

			dot.setAttribute("data-index", i);
			dot.addEventListener("click", dotHandler.bind(this));
			dots.appendChild(dot);
		}

		this._next = next;
		this._prev = prev;
		this._elements.nav.appendChild(prev);
		this._elements.nav.appendChild(dots);
		this._elements.nav.appendChild(next);
		this._elements.dots = dots;

		function dotHandler(e) {
			var index = e.target.getAttribute("data-index");

			this._currentIndex = index;
			this._changeSlide(0);
		}
	}

	_changeSlide(direction) {
		if(direction === -1) {
			this._currentIndex++;
		}
		if(direction === 1){
			this._currentIndex--;
		}
		if(direction === 0) {
			this._currentIndex = this._currentIndex;
		}

		if(this._currentIndex < 0) {
			this._currentIndex = 0;
		}

		if(this._currentIndex > this._data.length - 1) {
			this._currentIndex = this._data.length - 1;
		}
		
		this._elements.items.style.marginLeft = (this._currentIndex * -1) * this._width + "px";
		this._changeBackground();
		this._changeLink();
		this._changeActiveDot();
	}

	_changeBackground() {
		var image = this._data[this._currentIndex].background;

		this._elements.background.style.backgroundImage = `url(${image})`;
	}

	_changeLink() {
		var link = this._data[this._currentIndex].link;

		this._elements.link.href = link;
	}

	_changeActiveDot() {
		var dots = this._elements.dots.children;

		for(var i = 0; i < dots.length; i++) {
			var dot = dots[i];

			dot.classList.remove("slider__dot--active");
		}

		dots[this._currentIndex].classList.add("slider__dot--active");
	}

	_init() {
		this._data = this._getDataItems();
		this._width = this._getWidth();
		this._setItemWidth(this._width);
		this._elements.items.style.width = this._width * (this._elements.items.children.length + 1) + "px";
		this._createNavItems();
		this._changeBackground();
		this._changeLink();
		this._changeActiveDot();
		this._next.addEventListener("click", this._onClick.bind(this, -1));
		this._prev.addEventListener("click", this._onClick.bind(this, 1));
	}
}

