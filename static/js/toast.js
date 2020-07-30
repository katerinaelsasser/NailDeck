const toast = new iqwerty.toast.Toast();
toast.setText('This is a basic toast message!')
.stylize({
  background: 'pink',
  color: 'black',
  'box-shadow': '0 0 50px rgba(0, 0, 0, .7)'
.show();


toastr.options = {
  "closeButton": false,
  "debug": false,
  "newestOnTop": false,
  "progressBar": false,
  "positionClass": "toast-top-right",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
}