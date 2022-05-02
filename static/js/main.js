var owlProduct;

$(document).ready(function() {

    let owlProduct = $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        responsive:{
            0:{
                items:1
            }
        },
        dotsContainer: '#carousel-custom-dots'
    })



});