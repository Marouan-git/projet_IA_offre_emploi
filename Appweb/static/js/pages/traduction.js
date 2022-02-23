function customPopup() {

  let $btnShowPopup = $('.js-open-popup');
  let $btnClosePopup = $('.js-close-popup');
  let $popup = $('.js-custom-popup');

  $btnShowPopup.on('click', function () {

      let targetPopup = $(this).attr('data-target');
      $("[data-popup=" + targetPopup + "]").addClass('is-active');

  });

  $btnClosePopup.on('click', function () {
      $(this).parents('.is-active').removeClass('is-active');
  });

  $popup.on('click', function (event) {
      if (!$(event.target).closest('.js-custom-popup-holder').length && !$(event.target).is('js-custom-popup')) {
          if ($popup.hasClass('is-active')) {
              $popup.removeClass('is-active');
          }
      }
  });

}
customPopup();