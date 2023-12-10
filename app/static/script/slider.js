const swiper = new Swiper('.swiper-container', {
  direction: 'horizontal',
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  slidesPerView: 1,
  centeredSlides: true,
  effect: 'coverflow', // Use coverflow effect
  coverflowEffect: {
    rotate: 50, // Set rotation degree
    stretch: 0, // Set stretching factor
    depth: 100, // Set depth
    modifier: 1, // Set the zoom level
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  scrollbar: {
    el: '.swiper-scrollbar',
  },
});
