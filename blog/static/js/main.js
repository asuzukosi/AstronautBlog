$(function() {
	
	$('.input-group').find('.form-control').focus(function(){
		$(this).closest('.input-group').addClass("input-group-focus");
	}).blur(function() {
		$(this).closest('.input-group').removeClass("input-group-focus");
	});

	var slider = document.getElementById('slider');

	noUiSlider.create(slider, {
	    start: [20, 80],
	    connect: true,
	    range: {
	        'min': 0,
	        'max': 100
	    }
	});

	var slider2 = document.getElementById('slider-2');

	noUiSlider.create(slider2, {
	    start: [30],
	    connect: [true, false],
	    range: {
	        'min': 0,
	        'max': 100
	    }
	});


	$('.dropdown > a').click(function() {

		let $this = $(this);

		if ( $this.closest('.dropdown').find('.dropdown-menu').hasClass('active') ) {
			$this.closest('.dropdown').find('.dropdown-menu').removeClass('active');
		}

		setTimeout(function() {
			$this.closest('.dropdown').find('.dropdown-menu').addClass('active')
		}, 100);

	});


	$('#datetimepicker1').datetimepicker();

	$('[data-toggle="popover"]').popover();

  $('[data-toggle="tooltip"]').tooltip()



});