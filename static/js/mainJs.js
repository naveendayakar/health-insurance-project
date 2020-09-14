function checkDate() {
  var today = new Date().toISOString().split('T')[0];
  document.getElementById("date_of_incidence").setAttribute('max',today);
}
function checkDateBirth() {
    var today = new Date().toISOString().split('T')[0];
    document.getElementById("date_of_birth").setAttribute('max',today);
  }
